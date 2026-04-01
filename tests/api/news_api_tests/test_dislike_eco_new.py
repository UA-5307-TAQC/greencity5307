"""Validation of request for dislike eco new"""
# pylint: disable=duplicate-code
import allure
import pytest
from jsonschema import validate, ValidationError

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "news_id, status_code, message", [
        ("1", 404, "Eco new doesn't exist by this id: 1"),
        ("32", 200, ""),
        ("2", 404, "Eco new doesn't exist by this id: 2"),
        ( "77", 404, "Eco new doesn't exist by this id: 77"),
        ("90", 200, "")
]

)

@allure.feature("DislikeEcoNew")
@allure.story("Dislike eco new")
@allure.title("Dislike eco new by id.")
def test_dislike_eco_new(news_id, status_code, message, access_token):
    """Test of dislike of eco new"""
    client = EcoNewClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.dislike_eco_news_by_id(news_id=news_id)
    if response.status_code == 200:
        if response.content:
            with allure.step("Validate proper response json format"):
                parsed_data = response.json()
                logger.info(parsed_data)
                try:
                    validate(instance=parsed_data, schema=one_news_get_by_id_schema)
                    logger.info("JSON validation passed")
                except ValidationError as e:
                    allure.attach(str(e), name="Validation Error",
                          attachment_type=allure.attachment_type.TEXT)
                    pytest.fail(f"Response JSON does not match schema: {e}")
                else:
                    pytest.fail(f"Response JSON does not match schema: {status_code}")

    else:
        assert response.status_code == status_code, \
            f"Expected status code {status_code}, got {response.status_code}"
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == message, \
            f"Expected message '{message}', got '{parsed_data["message"]}"
