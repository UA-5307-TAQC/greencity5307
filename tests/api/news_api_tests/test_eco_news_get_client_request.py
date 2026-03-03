import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from jsonschema import validate

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.eco_news_response_schema import eco_news_response_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "page, size, message, status_code",
    [
        (-1, 20, "page must be a positive number", 400),
        (1, -1, "size must be a positive number", 400),
        (1, 0, "Page size must be greater than or equal to 1", 400),
        (1, 101, "Page size must be less than or equal to 100", 400),
    ],
)
@allure.feature("News")
@allure.story("Get news")
@allure.title("Verify proper responses when use invalid query params")
def test_eco_news_get_request_with_invalid_query_params(page: int,
                                                        size: int,
                                                        message: str,
                                                        status_code: int):
    """Test eco news request expecting error"""

    client = EcoNewClient(base_url=Config.BASE_API_URL)

    response = client.find_eco_news_by_page(
        page=page,
        size=size
    )
    with allure.step("Check status code"):
        logger.info(response.status_code)
        assert response.status_code == status_code

    with allure.step("Validate proper response message"):
        logger.info(response.text)
        assert response.text == f'{{"message":"{message}"}}'


@pytest.mark.parametrize(
    "page, size",
    [
        (10, 12),
        (0, 20),
        (0, 30),
        (0, 100),
        (100, 100),
    ],
)
@allure.feature("News")
@allure.story("Get news")
@allure.title(
    "Test eco news get request's response returns correct data format")
def test_eco_news_get_request(page: int, size: int):
    """Test like one news page like one news"""

    client = EcoNewClient(base_url=Config.BASE_API_URL)

    response = client.find_eco_news_by_page(
        page=page,
        size=size
    )

    with allure.step("Check status code"):
        logger.info(response.status_code)
        assert response.status_code == 200

    with allure.step("Validate proper response json format"):
        parsed_data = response.json()
        logger.info(parsed_data)
        try:
            validate(instance=parsed_data, schema=eco_news_response_schema)
            logger.info("✅ JSON validation passed")
        except Exception as e:
            logger.error(f"❌ JSON validation failed: {e}")
            allure.attach(str(e), name="Validation Error",
                          attachment_type=allure.attachment_type.TEXT)
            pytest.fail(f"Response JSON does not match schema: {e}")
