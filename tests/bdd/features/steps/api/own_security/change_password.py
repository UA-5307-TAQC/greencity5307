"""Change password test case"""
from behave import given, when, then
from jsonschema import validate, ValidationError

from clients.own_security_client import OwnSecurityClient
from data.config import Config
from schemas.own_security.update_password_negative_scenarios import status_code_400_schema, status_code_401_schema
from tests.api.conftest import login_user  # pylint: disable=import-error, no-name-in-module

# --- GIVEN ---

@given('the user is authenticated with a valid access token')
def step_implementation_with_token(context):
    """get access token"""
    access_token = login_user()
    context.client = OwnSecurityClient(Config.BASE_USER_API_URL, access_token)

@given('the user is unauthenticated (no access token provided)')
def step_implementation_without_token(context):
    """ run without authentication """
    context.client = OwnSecurityClient(Config.BASE_USER_API_URL, access_token=None)

# --- WHEN ---

@when(
    'the user sends a PUT request to change the password with "{new_password}" '
    'and confirm password "{confirm_password}"')
@when(
    'the user sends a PUT request to change the password with new password "{new_password}" '
    'and confirm password "{confirm_password}"')
def step_implementation_change_password(context, new_password, confirm_password):
    """Change password and confirm password"""
    if confirm_password == "[empty]":
        confirm_password = ""

    context.response = context.client.change_password(
        password=new_password,
        confirm_password=confirm_password
    )

# --- THEN ---

@then('the response status code should be {expected_status:d}')
def check_status_code(context, expected_status):
    """check valid status code"""
    actual_status = context.response.status_code
    assert actual_status == expected_status, \
        f"Expected {expected_status}, got {actual_status}. Response: {context.response.text}"

@then('the response time should be less than {time_limit:d} ms')
def check_ms(context, time_limit):
    """check ms response"""
    response_time_ms = context.response.elapsed.total_seconds() * 1000
    assert response_time_ms < time_limit, f"API response is too slow! Time: {response_time_ms:.2f} ms"

@then('the response body should be empty or "{empty_json}"')
def check_body_implementation(context, empty_json):
    """check empty body or empty json"""
    body = context.response.text.strip()
    assert body in ["", empty_json], f"Expected empty body or '{empty_json}', but got: {context.response.text}"

@then('the response matches the 400 Bad Request JSON schema')
def check_schema_validation_400(context):
    """compare schema validation"""
    try:
        validate(instance=context.response.json(), schema=status_code_400_schema)
    except ValidationError as e:
        raise AssertionError(f"JSON Schema validation failed for 400: {e.message}\nPath: {list(e.path)}") from e

@then('the response matches the 401 Unauthorized JSON schema')
def check_schema_validation_401(context):
    """compare schema validation"""
    try:
        validate(instance=context.response.json(), schema=status_code_401_schema)
    except ValidationError as e:
        raise AssertionError(f"JSON Schema validation failed for 401: {e.message}\nPath: {list(e.path)}") from e

@then('the response error message should contain "{expected_error_text}"')
def check_error_message(context, expected_error_text):
    """show error message"""
    actual_error_message = str(context.response.json()).lower()
    assert expected_error_text.lower() in actual_error_message, \
        f"Expected error to contain '{expected_error_text}', but got: {context.response.json()}"
