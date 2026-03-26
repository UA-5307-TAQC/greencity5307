import allure
import pytest
from jsonschema import validate

from clients.greencity_user_api.user_client import UserClient
from schemas.greencity_user_api.user.user_update_dto_schema import \
    user_update_dto_schema
from utils.logger import logger


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Get User dto by principal (email) from access token")
@allure.title("Verify response with access token")
def test_get_user_dto_by_principal_from_access_token(access_token):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token=access_token)
    response = client.get_user_dto_by_principal_from_access_token()
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)


    if status_code == 200:
        with allure.step("Validate successful response"):
            parsed_data = response.json()
            logger.info("RESPONSE DATA: %s", parsed_data)
            try:
                validate(instance=parsed_data, schema=user_update_dto_schema)
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
@allure.story("Get User dto by principal (email) from access token")
@allure.title("Verify response with wrong access token")
def test_get_user_dto_by_principal_from_not_valid_access_token():
    """Test get user dto by principal from access token"""

    client = UserClient(access_token="not_access_token")
    response = client.get_user_dto_by_principal_from_access_token()
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)


    if status_code == 401:
        with allure.step("Validate unauthorized error"):
            parsed_error = response.json()
            logger.info('Error: %s', parsed_error)
            assert parsed_error[
                       'error'] == "Unauthorized", "Wrong error message"
    else:
        pytest.fail(f"Unhandled error")
