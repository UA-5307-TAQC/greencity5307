import allure
import pytest
from jsonschema import validate

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "news_id, lang",
    [
        (1, 'en'),
        (2, 'en'),
        (3, 'en'),
        (4, 'en'),
        (5, 'en'),
        (6, 'en'),
        (7, 'en'),
        (17, 'en'),
        (77, 'en'),
        (56, 'en'),
        (90, 'en'),
        (734, 'en'),
        (4044, 'en'),
        (1, 'uk'),
        (2, 'uk'),
        (3, 'uk'),
        (4, 'uk'),
        (5, 'uk'),
        (6, 'uk'),
        (7, 'uk'),
        (17, 'uk'),
        (77, 'uk'),
        (56, 'uk'),
        (90, 'uk'),
        (734, 'uk'),
        (4044, 'uk'),
        (1, 'not-exist'),
        (2, 'not-exist'),
        (3, 'not-exist'),
        (4, 'not-exist'),
        (5, 'not-exist'),
        (6, 'not-exist'),
        (7, 'not-exist'),
        (17, 'not-exist'),
        (77, 'not-exist'),
        (56, 'not-exist'),
        (90, 'not-exist'),
        (734, 'not-exist'),
        (4044, 'not-exist'),
    ],
)
@allure.feature("News")
@allure.story("Get news")
@allure.title(
    "Test eco news get request's response returns correct data format")
def test_get_eco_news_by_id(news_id: int, lang: str):
    """Test like one news page like one news"""

    client = EcoNewClient(base_url=Config.BASE_API_URL)

    response = client.find_eco_news_by_id(news_id=news_id, lang=lang)

    status_code = response.status_code
    logger.info(status_code)

    if status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=one_news_get_by_id_schema)
                logger.info("✅ JSON validation passed")
            except Exception as e:
                logger.error(f"❌ JSON validation failed: {e}")
                allure.attach(str(e), name="Validation Error",
                              attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Response JSON does not match schema: {e}")
    elif status_code == 400:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == "Select correct language: \'en\' or \'ua\'"
        assert response.text == f'{{"message":"Select correct language: \'en\' or \'ua\'"}}'
    elif status_code == 404:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert response.text == f'{{"message":"Eco new doesn\'t exist by this id: {news_id}"}}'
    else:
        assert False, "Other error"
