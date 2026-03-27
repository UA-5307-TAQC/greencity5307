import allure
import pytest
from jsonschema import validate

from clients.greencity_user_api.user_client import UserClient
from schemas.greencity_user_api.user import pageable_dto_user_for_list_schema
from utils.logger import logger

valid_data = [
    # ✅ Default values (no params)
    ({}, {"searchReg": ""}),

    # ✅ Valid values
    ({"page": 0, "size": 5}, {"searchReg": "test"}),
    ({"page": 1, "size": 10}, {"searchReg": "john"}),

    # ✅ Boundary values
    ({"page": 0, "size": 1}, {"searchReg": ""}),
    ({"page": 10, "size": 100}, {"searchReg": "abc"}),
]
invalid_data = [
    # ⚠️ Page edge cases
    ({"page": -1, "size": 5}, {"searchReg": ""}),
    # should fallback to default page=0
    ({"page": None, "size": 5}, {"searchReg": ""}),

    # ⚠️ Size edge cases
    ({"page": 0, "size": 0}, {"searchReg": ""}),
    # fallback to default size=5
    ({"page": 0, "size": 101}, {"searchReg": ""}),  # capped to 100

    # ⚠️ Missing params individually
    ({"page": 2}, {"searchReg": "test"}),
    ({"size": 20}, {"searchReg": "test"}),

    # ⚠️ Sorting
    ({"sort": "asc"}, {"searchReg": ""}),
    ({"sort": "desc"}, {"searchReg": ""}),
    ({"sort": "name"}, {"searchReg": ""}),  # default asc
    ({"sort": "name,asc&sort=email,desc"}, {"searchReg": ""}),

    # ❌ Invalid types (depending on API validation)
    ({"page": "abc", "size": 5}, {"searchReg": ""}),
    ({"page": 0, "size": "big"}, {"searchReg": ""}),

    # ❌ Invalid sort format
    ({"sort": "wrong_format"}, {"searchReg": ""}),
]


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Filter all user by search criteria")
@allure.title("Verify response with access token")
@pytest.mark.parametrize("query, json", valid_data)
def test_filter_all_user_by_search_criteria(query, json, access_token):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token=access_token)
    response = client.filter_all_user_by_search_criteria(**query, **json)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)

    if status_code == 200:
        with allure.step("Validate successful response"):
            parsed_data = response.json()
            logger.info("RESPONSE DATA: %s", parsed_data)
            try:
                validate(instance=parsed_data,
                         schema=pageable_dto_user_for_list_schema)
            except Exception as e:
                pytest.fail(f"Response JSON does not match schema: {e}")
    elif status_code == 403:
        with allure.step("Validate 403 error"):
            parsed_error = response.json()
            logger.info('Error: %s', parsed_error)
            assert parsed_error[
                       'error'] == "Forbidden", "Wrong authorization error message"
    else:
        pytest.fail(f"Unhandled error")


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Filter all user by search criteria")
@allure.title("Verify response without access token")
@pytest.mark.parametrize("query, json", valid_data)
def test_filter_all_user_by_search_criteria_not_valid_access_token(query,
                                                                   json):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token="not_access_token")
    response = client.filter_all_user_by_search_criteria(**query, **json)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)

    assert status_code == 401, "Wrong response"


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Filter all user by search criteria")
@allure.title("Verify invalid response")
@pytest.mark.parametrize("query, json", invalid_data)
def test_filter_all_user_by_search_criteria_invalid_params(query, json,
                                                           access_token):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token=access_token)
    response = client.filter_all_user_by_search_criteria(**query, **json)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)

    assert status_code == 400, "Wrong response"
