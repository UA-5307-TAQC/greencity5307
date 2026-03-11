"""Test Create Eco News form with valid data."""

import tempfile



import allure
import pytest
from PIL import Image
from jsonschema import validate


from clients.create_eco_news_client import CreateEcoNewsClient
from data.config import Config
from schemas.news.create_new_schema import create_eco_new_schema


def image_file():
    """Helper function to provide a test image file path."""
    with allure.step("Test image file path"):
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
            img = Image.new("RGB", (10, 10), color="green")
            img.save(tmp.name)
            return tmp.name


@pytest.mark.parametrize(
    "data",
    [
        {
            "source": "https://example.org",
            "shortInfo": "Climate change update",
            "tags": ["news", "events"],
            "title": "Climate change update",
            "text": "Full article text here",
            "titleTranslation": {
                "content": "Climate News",
                "languageCode": "en"
        },
            "textTranslation": {
                "content": "Full article text here",
                "languageCode": "en"
            }
        },
        {
            "source": "https://example.com",
            "shortInfo": "New eco-friendly product launch",
            "tags": ["education", "ads"],
            "title": "New eco-friendly product launch",
            "text": "Full article text here",
            "titleTranslation": {
                "content":"Eco Product Launch",
                "languageCode":"en"
            },
            "textTranslation": {
                "content":"Details about the new product",
                "languageCode":"en"
            }
        },
        {
            "source": "https://example.net",
            "shortInfo": "Upcoming environmental event",
            "tags": ["events"],
            "title": "Upcoming environmental event",
            "text": "Full article text here",
            "titleTranslation": {
                "content":"Environmental Event",
                "languageCode":"en"
            },
            "textTranslation": {
                "content":"Event details and registration info",
                "languageCode":"en"
            }
        }
    ],
)

@allure.feature("CreateEcoNews")
@allure.story("Create new")
@allure.title("Create eco new by applying valid parameters to the form.")
def test_create_eco_news_post_request_with_valid_data(data: dict, access_token):
    """Test create eco news request with valid data"""
    token = access_token

    client = CreateEcoNewsClient(
        base_url=Config.BASE_API_URL,
        access_token=token
    )


    response = client.create_eco_news_by_data(
        image_file_path=image_file(),
        data=data
    )

    with allure.step("Check status code"):
        assert response.status_code == 201, response.text

    with allure.step("Validate proper response json format"):
        parsed_data = response.json()
        validate(instance=parsed_data, schema=create_eco_new_schema)
