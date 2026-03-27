import allure
import pytest
from jsonschema import validate

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.eco_news_response_schema import eco_news_response_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "page, size, sort, message, status_code",
    [
        (-1, 20, None, "page must be a positive number", 400),
        (0, -1, None, "size must be a positive number", 400),
        (0, 0, None, "Page size must be greater than or equal to 1", 400),
        (0, 101, None, "Page size must be less than or equal to 100", 400),
        (0, 20, ['not-created'],
         "Unsupported value for sorting: [not-created]", 400),
        (0, 20, ['not-created', 'not-created-2'],
         "Invalid value 'not-created-2' for orders given; "
         "Has to be either 'desc' or 'asc' (case insensitive)",
         400),
    ],
)
@allure.epic("Greencity API")
@allure.feature("News")
@allure.story("Get news page")
@allure.title("Verify proper responses when use invalid query params")
def test_find_eco_news_by_page_request_with_invalid_query_params(page: int,
                                                                 size: int,
                                                                 sort: list[
                                                                     str] | None,
                                                                 message: str,
                                                                 status_code: int):
    """Test eco news request expecting error"""

    client = EcoNewClient(base_url=Config.BASE_API_URL)

    response = client.find_eco_news_by_page(
        page=page,
        size=size,
        sort=sort,
    )
    with allure.step("Check status code"):
        logger.info(response.status_code)
        assert response.status_code == status_code

    with allure.step("Validate proper response message"):
        parsed_error = response.json()
        logger.info(parsed_error)
        assert parsed_error.get("message") == message


@pytest.mark.parametrize(
    "page, size, tags, title, author_id, favorite",
    [
        (0, 20, None, None, None, False),
        (10, 12, ['news', 'education'], None, None, False),
        (0, 30, None, 'Test', None, False),
        (0, 100, None, None, 1, False),
        (100, 100, None, None, None, False),
        (0, 20, None, None, 1, True),
        (0, 20, None, 'Test', 1, False),
        (0, 20, None, 'Test', 1, True),
        (0, 20, ['events'], 'Test', 1, False),
        (0, 20, None, None, 1000000, False),
        (0, 20, ['not-exist'], None, 1000000, False),
        (0, 20, None, 'Not-exist', 1000000, False),
    ],
)
@allure.epic("Greencity API")
@allure.feature("News")
@allure.story("Get news page")
@allure.title(
    "Test eco news get request's response returns correct data format")
def test_find_eco_news_by_page_request(page: int,
                                       size: int,
                                       tags: list[str],
                                       title: str,
                                       author_id: int,
                                       favorite: bool):
    """Validate 200 OK response and eco news JSON schema for find_eco_news_by_page with various filters."""

    client = EcoNewClient(base_url=Config.BASE_API_URL)

    response = client.find_eco_news_by_page(
        page=page,
        size=size,
        tags=tags,
        title=title,
        author_id=author_id,
        favorite=favorite,
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
