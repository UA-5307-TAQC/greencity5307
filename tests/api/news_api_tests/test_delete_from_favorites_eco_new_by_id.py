"""Test validation of deletion from favorites of eco new"""

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

@allure.feature("AddToFavoritesEcoNew")
@allure.story("Add to favorites eco new")
@allure.title("Add to favorites eco new by id.")
def test_delete_from_favorites_by_id(news_id, access_token):
    """Test of addition to favorites of eco new"""
    client = EcoNewClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.delete_from_favorites_eco_new_by_id(news_id=news_id)
    if response.status_code == 201:
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
    elif response.status_code == 200:
        with allure.step("Validate proper response json format"):
            assert not response.text
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
