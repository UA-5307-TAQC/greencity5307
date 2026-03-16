"""Validation of request for summary eco new"""
# pylint: disable=duplicate-code
import allure
import pytest
from jsonschema import validate, ValidationError

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "news_id", [
        "1", "32", "2", "77", "90"
    ]
)

@allure.feature("GetRecommendedEcoNew")
@allure.story("Get recommended eco new")
@allure.title("Get recommended eco new by id.")
def test_eco_new_summary(news_id, access_token):
    """Test of dislike of eco new"""
    client = EcoNewClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.get_recommended_eco_news(news_id=news_id)
    if response.status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                for news in parsed_data:
                    validate(instance=news, schema=one_news_get_by_id_schema)
                    logger.info("JSON validation passed")
            except ValidationError as e:
                allure.attach(str(e), name="Validation Error",
                              attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Response JSON does not match schema: {e}")
    elif response.status_code == 400:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == "User has already added this eco new to favorites."
    elif response.status_code == 404:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == f"Eco new doesn\'t exist by this id: {news_id}"
    elif response.status_code == 403:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["error"] == "Forbidden"
    elif response.status_code == 500:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data.get("error") == "Internal Server Error"
    else:
        assert False, "Other error"
