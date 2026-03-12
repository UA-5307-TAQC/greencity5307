"""Validation of updating eco new by id"""
# pylint: disable=duplicate-code
import tempfile

import allure
import pytest
from PIL import Image
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from utils.logger import logger


def image_file():
    """Helper function to provide a test image file path."""
    with allure.step("Test image file path"):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            img = Image.new("RGB", (10, 10), color="green")
            img.save(tmp.name)
            return tmp.name

@pytest.mark.parametrize(
    "news_id, data",
    [
        ("32",{
            "id" : "32",
            "source": "https://example.org",
            "shortInfo": "Climate change update",
            "tags": ["news", "events"],
            "title": "Climate change update",
            "content": "Full article text here",
            "titleTranslation": {
                "content": "Climate News",
                "languageCode": "en"
        },
            "textTranslation": {
                "content": "Full article text here",
                "languageCode": "en"
            }
        }),
        ("45", {
            "id" : "45",
            "source": "https://example.com",
            "shortInfo": "New eco-friendly product launch",
            "tags": ["education", "ads"],
            "title": "New eco-friendly product launch",
            "content": "Full article text here",
            "titleTranslation": {
                "content":"Eco Product Launch",
                "languageCode":"en"
            },
            "textTranslation": {
                "content":"Details about the new product",
                "languageCode":"en"
            }
        }),
        ("78", {
            "id" : "78",
            "source": "https://example.net",
            "shortInfo": "Upcoming environmental event",
            "tags": ["events"],
            "title": "Upcoming environmental event",
            "content": "Full article text here",
            "titleTranslation": {
                "content":"Environmental Event",
                "languageCode":"en"
            },
            "textTranslation": {
                "content":"Event details and registration info",
                "languageCode":"en"
            }
        })
    ],
)

@allure.feature("UpdateEcoNew")
@allure.story("Update new")
@allure.title("Update eco new by applying valid parameters to the form.")
def test_update_eco_news_put_request_with_valid_data(news_id, data: dict, access_token):
    """Test create eco news request with valid data"""
    token = access_token

    client = EcoNewClient(
        base_url=Config.BASE_API_URL,
        access_token=token
    )


    response = client.update_eco_news_by_id(
        news_id=news_id,
        image_file_path=image_file(),
        data=data
    )

    if response.status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=one_news_get_by_id_schema)
                logger.info("✅ JSON validation passed")
            except ValidationError as e:
                allure.attach(str(e), name="Validation Error",
                              attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Response JSON does not match schema: {e}")
    elif response.status_code == 400:
        parsed_data = response.json()
        logger.info(parsed_data)

        assert parsed_data["message"] == "Current user has no permission for this action"
    elif response.status_code == 404:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == f"Eco new doesn\'t exist by this id: {news_id}"
    else:
        assert False, "Other error"
