import json
from collections import defaultdict
from jsonschema import Draft7Validator

import pytest
import allure

from clients.friends_client import FriendsClient
from clients.own_security_client import OwnSecurityClient

from data.config import Config


@pytest.fixture(scope="function")
def access_token():
    """Fixture that logs in the user for api tests."""
    client = OwnSecurityClient(Config.BASE_USER_API_URL)
    response = client.sign_in(
        email=Config.USER_EMAIL,
        password=Config.USER_PASSWORD
    )

    assert response.status_code == 200, \
        f"Login failed. Status: {response.status_code}. Response body: {response.text}"

    auth_token = response.json().get("accessToken")
    assert auth_token, \
        f"Login response does not contain access token. Response body: {response.text}"

    return auth_token


@pytest.fixture(scope="function")
def dynamic_friend_id(access_token):
    """Fixture that returns a valid confirmed friend id for current user. """

    client = FriendsClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.get_all_friends()
    assert response.status_code == 200, (f"Failed to fetch friends for fixture, "
                                         f"status code: {response.status_code}")

    data = response.json()
    friends_list = data.get("page", [])

    if not friends_list:
        pytest.skip("Test skipped: No confirmed friends found for current user.")

    return friends_list[0].get("id")


@pytest.fixture(scope="function")
def validate_json():
    def _log_json_errors(schema, data):
        allure.attach(
            json.dumps(data, indent=2),
            name="Full Response Body",
            attachment_type=allure.attachment_type.JSON
        )
        validator = Draft7Validator(schema)
        errors = list(validator.iter_errors(data))

        if errors:
            grouped_errors = defaultdict(list)
            for err in errors:
                index = err.path[0] if err.path else "General"
                grouped_errors[index].append(err)

            for index, err_list in grouped_errors.items():

                report_lines = []
                for i, err in enumerate(err_list, 1):
                        path = " -> ".join(map(str, list(err.path)[1:])) or "root"
                        report_lines.append(f"{i}. [{path}] -> {err.message} (Actual: {err.instance})")

                allure.attach(
                    "\n".join(report_lines),
                    name=f"JSON Schema Mismatch: Record #{index}",
                    attachment_type=allure.attachment_type.TEXT
                )

            assert False, f"JSON validation failed. Found {len(grouped_errors)} schema errors"

    return _log_json_errors
