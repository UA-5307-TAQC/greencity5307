import allure
import pytest

from clients.greencity_user_api.user_client import UserClient
from utils.logger import logger

valid_data = [
    (
        {
            "name": "Іван Петренко",
            "email": "ivan@example.com",
            "role": "ROLE_USER",
            "userStatus": "VERIFIED"
        },
        200
    ),
    (
        {
            "name": "John-Doe",
            "email": "john.doe@test.com",
            "role": "ROLE_ADMIN",
            "userStatus": "CREATED"
        },
        200
    ),
    (
        {
            "name": "Марія",
            "email": "maria@test.com",
            "role": "ROLE_EMPLOYEE",
            "userStatus": "VERIFIED"
        },
        200
    ),
]
invalid_data = [
    # invalid name (double dots)
    (
        {
            "name": "Іван..Петро",
            "email": "ivan@test.com",
            "role": "ROLE_USER",
            "userStatus": "VERIFIED"
        },
        400
    ),
    # invalid name (ends with dot)
    (
        {
            "name": "Іван.",
            "email": "ivan@test.com",
            "role": "ROLE_USER",
            "userStatus": "VERIFIED"
        },
        400
    ),
    # invalid role
    (
        {
            "name": "Іван",
            "email": "ivan@test.com",
            "role": "ROLE_SUPER_ADMIN",
            "userStatus": "VERIFIED"
        },
        400
    ),
    # invalid userStatus
    (
        {
            "name": "Іван",
            "email": "ivan@test.com",
            "role": "ROLE_USER",
            "userStatus": "DELETED"
        },
        400
    ),
    # missing required field (email)
    (
        {
            "name": "Іван",
            "email": None,
            "role": "ROLE_USER",
            "userStatus": "VERIFIED"
        },
        400
    ),
]


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Update user by UserManagement")
@allure.title("Verify response with access token")
@pytest.mark.parametrize("payload, expected_status", valid_data + invalid_data)
def test_update_user_by_user_management(payload, expected_status,
                                        access_token):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token=access_token)
    response = client.update_user_by_user_management(**payload)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)
    logger.info("DATA: %s", response.json())

    assert status_code == expected_status, "Wrong response"

@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Update user by UserManagement")
@allure.title("Verify response without access token")
@pytest.mark.parametrize("payload, expected_status", valid_data)
def test_update_user_by_user_management_not_valid_access_token(payload, expected_status):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token="not_access_token")
    response = client.update_user_by_user_management(**payload)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)
    logger.info("DATA: %s", response.json())

    assert status_code == 401, "Wrong response"
