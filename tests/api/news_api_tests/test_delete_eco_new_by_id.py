"""Test for validation of DELETE request for delete of eco new."""
from json import JSONDecodeError

import allure
import pytest
from jsonschema import validate

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "news_id", [
        "1", "32", "2", "77", "90"
    ]
)
@allure.feature("DeleteEcoNew")
@allure.story("Delete new")
@allure.title("Delete eco new by id.")
def test_delete_eco_new_by_id(access_token, news_id: int):
    """Test for validation of correctness of DELETE request."""
    client = EcoNewClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.delete_eco_news_by_id(news_id=news_id)
    if response.status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=one_news_get_by_id_schema)
                logger.info("✅ JSON validation passed")
            except JSONDecodeError as e:
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
