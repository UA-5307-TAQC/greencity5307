"""Test password update API"""
import pytest
import allure
from jsonschema import validate, ValidationError

from clients.own_security_client import OwnSecurityClient
from data.config import Config
from schemas.own_security.update_password_negative_scenarios import status_code_400_schema, status_code_401_schema


@allure.title("Successful password update with valid and matching inputs")
def test_password_update(access_token):
    """Test successful password update and safely restore original state"""

    client = OwnSecurityClient(Config.BASE_USER_API_URL, access_token)

    try:
        with allure.step("Send PUT request to change password"):
            response = client.change_password(
                password="NewstrongPassword1!",
                confirm_password="NewstrongPassword1!"
            )

        with allure.step("Validate status code and response time"):
            assert response.status_code == 200, (f"Expected status code 200, but got {response.status_code}. "
                                                 f"Response: {response.text}")

            response_time_ms = response.elapsed.total_seconds() * 1000
            assert response_time_ms < 3000, f"API response is too slow! Time: {response_time_ms:.2f} ms"

        with allure.step("Validate response body is empty or empty JSON"):
            assert response.text in ["", "{}"], f"Expected empty body or '{{}}', but got: {response.text}"

    finally:
        with allure.step("Teardown: Restore original password from Config"):
            restore_response = client.change_password(
                password=Config.USER_PASSWORD,
                confirm_password=Config.USER_PASSWORD
            )
            assert restore_response.status_code == 200, \
                (f"CRITICAL: Failed to restore original password! Subsequent tests might fail. "
                 f"Response: {restore_response.text}")

@allure.title("Password update validation: {scenario_name}")
@pytest.mark.parametrize(
    "scenario_name, new_password, confirm_password, expected_status, expected_error_text",
    [
        (
            "Mismatched passwords",
            "StrongPass1!", "DifferentPass2@",
            400, "The passwords don't match"
        ),
        (
            "Empty confirm password",
            "StrongPass1!", "",
            400, "must not be blank"
        ),
        (
            "Password too short",
            "123", "123",
            400, "password must be 8 or more characters in"
        ),
    ]
)
def test_password_update_negative_scenarios(
    access_token,
    scenario_name,
    new_password,
    confirm_password,
    expected_status,
    expected_error_text
):
    """Test various validation errors during password update"""

    client = OwnSecurityClient(Config.BASE_USER_API_URL, access_token)

    with allure.step(f"Send PUT request with parameters for: {scenario_name}"):
        response = client.change_password(
            password=new_password,
            confirm_password=confirm_password
        )

    with allure.step(f"Validate status code is {expected_status}"):
        assert response.status_code == expected_status, \
            f"Expected {expected_status}, got {response.status_code}. Response: {response.text}"

    with allure.step("Validate ERROR response schema and message"):
        data = response.json()
        schema_to_validate = status_code_400_schema
        if schema_to_validate:
            try:
                validate(instance=data, schema=schema_to_validate)
            except ValidationError as e:
                pytest.fail(
                    f"JSON Schema validation failed for status {expected_status}: {e.message}\nPath: {list(e.path)}")

    with allure.step("Validate ERROR response schema and message"):

        actual_error_message = str(data).lower()
        assert expected_error_text.lower() in actual_error_message, \
            f"Expected error to contain '{expected_error_text}', but got: {data}"


@allure.title("Unsuccessful password update attempt without authentication (401)")
def test_password_update_unauthorized():
    """Test that unauthenticated users cannot access the change password endpoint"""
    client = OwnSecurityClient(Config.BASE_USER_API_URL, access_token=None)

    with allure.step("Send PUT request without Authorization header"):
        response = client.change_password(
            password="NewstrongPassword1!",
            confirm_password="NewstrongPassword1!"
        )

    with allure.step("Validate status code is 401 Unauthorized"):
        assert response.status_code == 401, \
            f"Expected 401 Unauthorized, but got {response.status_code}. Response: {response.text}"

    with allure.step("Validate ERROR response schema and message"):
        data = response.json()
        schema_to_validate = status_code_401_schema
        if schema_to_validate:
            try:
                validate(instance=data, schema=schema_to_validate)
            except ValidationError as e:
                pytest.fail(
                    f"JSON Schema validation failed for status {data.status_code}: {e.message}\nPath: {list(e.path)}")


    with allure.step("Validate ERROR response schema and message"):

        actual_error_message = str(data).lower()
        expected_error_text = "unauthorized"

        assert expected_error_text in actual_error_message, \
            f"Expected error to contain '{expected_error_text}', but got: {data}"
