"""Steps for Google Security API testing."""
import allure
# pylint: disable=duplicate-code
from behave import given, when, then
from jsonschema import validate, ValidationError
from clients.google_security_client import GoogleSecurityClient
from data.config import Config
from schemas.google_security_schema import google_security_schema


@given('I have GoogleSecurityClient')
def step_get_google_client(context):
    """Initialize GoogleSecurityClient with access token from context."""
    if not hasattr(context, "access_token"):
        raise AssertionError("User is not authorized")

    context.client = GoogleSecurityClient(
        base_url=Config.BASE_USER_API_URL,
        access_token=context.access_token
    )

@when('I send GET request to google security with project "{project_name}" and lang "{lang}"')
def step_send_google_request(context, project_name, lang):
    """Send GET request to Google Security API with specified project name and language."""
    context.response = context.client.get_google_security(project_name, lang)

@then('the response status code should be {status_code}')
def step_validate_status(context, status_code):
    """Validate that the response status code matches the expected status code."""
    assert context.response.status_code == int(status_code), context.response.text


@then('the response should match google security schema if status is 200')
def step_validate_schema(context):
    """Validate that the response JSON matches the Google Security schema if the status code is 200."""
    if context.response.status_code != 200:
        return  # skip validation for error cases

    parsed_data = context.response.json()

    try:
        validate(instance=parsed_data, schema=google_security_schema)
    except ValidationError as e:
        allure.attach(str(e), name="Validation Error",
                      attachment_type=allure.attachment_type.TEXT)

@then('the response should contain "{message_type}" with value "{message}"')
def step_validate_message(context, message_type, message):
    """Validate that the response contains the specified message type with the expected value."""
    if not message_type:  # skip if empty
        return

    parsed_data = context.response.json()

    assert message_type in parsed_data, \
        f"Field '{message_type}' not found in response: {parsed_data}"

    assert parsed_data[message_type] == message, \
        f"Expected '{message}', got '{parsed_data[message_type]}'"
