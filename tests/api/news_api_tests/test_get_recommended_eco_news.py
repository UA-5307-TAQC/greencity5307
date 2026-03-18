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
    "news_id, status_code, message", [
        ("1", 200, ""),
        ("32", 200, ""),
        ("2", 200, ""),
        ( "77", 200, ""),
        ("90", 200, "")
]
)

@allure.feature("GetRecommendedEcoNew")
@allure.story("Get recommended eco new")
@allure.title("Get recommended eco new by id.")
def test_eco_new_summary(news_id,status_code, message, access_token):
    """Test summary get of eco new"""
    client = EcoNewClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.get_recommended_eco_news(news_id=news_id)
    if response.status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            for news in parsed_data:
                try:
                    validate(instance=news, schema=one_news_get_by_id_schema)
                    logger.info("JSON validation passed")
                except ValidationError as e:
                    allure.attach(str(e), name="Validation Error",
                          attachment_type=allure.attachment_type.TEXT)
                    pytest.fail(f"Response JSON does not match schema: {e}")

    else:
        assert response.status_code == status_code, \
            f"Expected status code {status_code}, got {response.status_code}"
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == message, \
            f"Expected message '{message}', got '{parsed_data["message"]}"
