"""sign in validation api test"""
import pytest
from behave import given, when, then
from jsonschema import validate, ValidationError

from clients.own_security_client import OwnSecurityClient
from data.config import Config
from schemas.own_security.signin_success_schema import signin_success_schema


@given('the user has valid credentials (email and password)')
def check_valid_credentials(_context):
    """empty method"""



@when('a POST request is sent to the "/ownSecurity/signIn" endpoint with the credentials payload')
def send_post_request(context):
    """send sign in request"""
    client = OwnSecurityClient(f"{Config.BASE_USER_API_URL}")
    context.response = client.sign_in(
        email=Config.USER_EMAIL,
        password=Config.USER_PASSWORD
    )
    context.data = context.response.json()


@then('the API should respond with a 200 OK status code')
def check_valid_status_code(context):
    """check response status code"""
    status_code = context.response.status_code
    assert status_code == 200, f"Expected status code 200, but got {status_code}"

@then('the response time should be less than {number:d} ms')
def check_valid_response_time(context, number):
    """check response time"""
    response_time_ms = context.response.elapsed.total_seconds() * 1000
    assert response_time_ms < number, f"API response is too slow! Time: {response_time_ms:.2f} ms"


@then('the schema should be the same as we have')
def check_valid_schema(context):
    """check schema should be the same as we have"""
    try:
        validate(instance=context.data, schema=signin_success_schema)
    except ValidationError as e:
        pytest.fail(f"Response body does not match signin_success_schema: {e.message}")


@then('the response body should contain a valid numeric "userId"')
def check_valid_userid(context):
    """check response body should contain a valid numeric 'userId'"""
    user_id = context.data.get("userId")
    assert user_id is not None and user_id >= 0, "User ID is invalid or missing"


@then('the response body should contain the name "Oleksandr"')
def check_valid_username(context):
    """check response body should contain the name 'Oleksandr'"""
    name = context.data.get("name")
    assert name == Config.USER_NAME, f"Expected {Config.USER_NAME}, but got '{name}'"


@then('the "ownRegistrations" flag in the response should be true')
def check_valid_ownregistrations(context):
    """check 'ownRegistrations' field"""
    assert context.data.get("ownRegistrations") is True, "ownRegistrations flag should be True"


@then('the "accessToken" must contain a future expiration timestamp ("exp")')
def check_expiration_accesstoken(context):
    """check expiration acccess token"""
    token = context.data.get("accessToken")
    assert token is not None, "Access token is missing in the response body"
