import allure
import pytest
from jsonschema import validate

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from utils.logger import logger

languages = ('en', 'uk')

@pytest.mark.parametrize(
    "news_id, lang",
    [
        (1, languages[0]),
        (2, languages[0]),
        (3, languages[0]),
        (4, languages[0]),
        (5, languages[0]),
        (6, languages[0]),
        (7, languages[0]),
        (17, languages[0]),
        (77, languages[0]),
        (56, languages[0]),
        (90, languages[0]),
        (734, languages[0]),
        (4044, languages[0]),
        (1, languages[1]),
        (2, languages[1]),
        (3, languages[1]),
        (4, languages[1]),
        (5, languages[1]),
        (6, languages[1]),
        (7, languages[1]),
        (17, languages[1]),
        (77, languages[1]),
        (56, languages[1]),
        (90, languages[1]),
        (734, languages[1]),
        (4044, languages[1]),
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
        # message contains `ua`, but should contain `uk`, this is API problem
        assert parsed_data["message"] == "Select correct language: \'en\' or \'ua\'"
    elif status_code == 404:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == f"Eco new doesn\'t exist by this id: {news_id}"
    else:
        assert False, "Other error"
