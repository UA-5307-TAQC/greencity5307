import allure
import pytest

from clients.greencity_user_api.user_client import UserClient
from utils.logger import logger

valid_data = [
    (
        {
            "name": "Іван Петренко",
            "emailNotification": "IMMEDIATELY"
        },
        200
    ),
    (
        {
            "name": "John Doe",
            "emailNotification": "DAILY"
        },
        200
    ),
    (
        {
            "name": "Марія-Анна",
            "emailNotification": "WEEKLY"
        },
        200
    ),
    (
        {
            "name": "Ivan O'Connor",
            "emailNotification": "MONTHLY"
        },
        200
    ),
]
invalid_data = [
    # double dot
    (
        {
            "name": "Іван..Петро",
            "emailNotification": "IMMEDIATELY"
        },
        400
    ),
    # ends with dot
    (
        {
            "name": "Іван.",
            "emailNotification": "IMMEDIATELY"
        },
        400
    ),
    # double dash
    (
        {
            "name": "Іван--Петро",
            "emailNotification": "DAILY"
        },
        400
    ),
    # invalid symbols
    (
        {
            "name": "Ivan@Petro!",
            "emailNotification": "WEEKLY"
        },
        400
    ),
    # too long name (>30 chars conceptually)
    (
        {
            "name": "І" * 40,
            "emailNotification": "MONTHLY"
        },
        400
    ),
    # invalid enum
    (
        {
            "name": "Іван Петренко",
            "emailNotification": "YEARLY"
        },
        400
    ),
    # missing required field
    (
        {
            "name": "Іван Петренко",
            "emailNotification": None
        },
        400
    ),
]


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Update user")
@allure.title("Verify response with access token")
@pytest.mark.parametrize("payload, expected_status", valid_data + invalid_data)
def test_update_user(payload, expected_status, access_token):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token=access_token)
    response = client.update_user(**payload)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)
    logger.info("DATA: %s", response.json())

    assert status_code == expected_status, "Wrong response"


@allure.epic("GreencityUser API")
@allure.feature("user-controller")
@allure.story("Update user")
@allure.title("Verify response without access token")
@pytest.mark.parametrize("payload, expected_status", valid_data)
def test_update_user_not_valid_access_token(payload, expected_status):
    """Test get user dto by principal from access token"""

    client = UserClient(access_token="not_access_token")
    response = client.update_user(**payload)
    status_code = response.status_code
    logger.info("STATUS CODE: %s", status_code)
    logger.info("DATA: %s", response.json())

    assert status_code == 401, "Wrong response"
