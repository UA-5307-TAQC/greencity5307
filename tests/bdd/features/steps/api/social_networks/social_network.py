"""Feature: Social Network Image Retrieval"""
import allure
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from behave import given, when, then

from clients.social_network_client import SocialNetworkClient
from data.config import Config
from schemas.social_networks_schema import social_networks_image_schema


@given('I have SocialNetworkClient')
def step_get_social_client(context):
    """Initialize SocialNetworkClient with access token from context."""
    if not hasattr(context, "access_token"):
        raise AssertionError("User is not authorized")

    context.client = SocialNetworkClient(
        base_url=Config.BASE_USER_API_URL,
        access_token=context.access_token
    )
@when('I send GET request to social network image with url "{image_url}"')
def step_get_image(context, image_url):
    """Send GET request to retrieve social network image using the specified URL."""
    context.response = context.client.get_image_social_networks(url=image_url)

@then('the response status code should be {status_code}')
def step_validate_status(context, status_code):
    """Validate that the response status code matches the expected status code."""
    assert context.response.status_code == int(status_code), context.response.text

@then('the response should match social network image schema')
def step_validate_image_schema(context):
    """Validate that the response JSON matches the social network image schema if the status code is 200."""
    if context.response.status_code != 200:
        raise AssertionError(
            f"Schema validation expected for 200, got {context.response.status_code}"
        )

    parsed_data = context.response.json()

    try:
        validate(instance=parsed_data, schema=social_networks_image_schema)
    except ValidationError as e:
        allure.attach(str(e), name="Validation Error",
                      attachment_type=allure.attachment_type.TEXT)

@then('the response should contain "{message_type}" with value "{message}"')
def step_validate_message(context, message_type, message):
    """Validate that the response contains the specified message type with the expected value."""
    parsed_data = context.response.json()

    assert message_type in parsed_data, \
        f"Field '{message_type}' not found in response: {parsed_data}"

    assert parsed_data[message_type] == message, \
        f"Expected '{message}', got '{parsed_data[message_type]}'"
