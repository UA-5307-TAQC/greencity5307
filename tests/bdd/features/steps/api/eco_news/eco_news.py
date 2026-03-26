"""Eco news api feature steps"""
import tempfile
import json
import allure
from behave import given, when, then

from jsonschema import validate, ValidationError

from PIL import Image

from clients.create_eco_news_client import CreateEcoNewsClient
from clients.eco_new_client import EcoNewClient
from clients.own_security_client import OwnSecurityClient
from data.config import Config
from schemas.news.one_news_schema import one_news_get_by_id_schema
from schemas.news.summary_eco_new_schema import summary_eco_new_schema
from utils.logger import logger


def create_test_image():
    """Method helper fot image generation"""
    with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as tmp:
        img = Image.new("RGB", (10, 10), color="green")
        img.save(tmp.name)
        return tmp.name

def validate_schema(data, schema):
    """Validation of schema"""
    try:
        validate(instance=data, schema=schema)
    except ValidationError as e:
        allure.attach(str(e), name="Validation Error",
                      attachment_type=allure.attachment_type.TEXT)

def login_user():
    """log in of the user"""
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

@given("I am an authorized user")
def step_authorized_user(context):
    """Authorization of the user"""
    context.access_token = login_user()
    context.client = EcoNewClient(
        base_url=Config.BASE_API_URL,
        access_token=context.access_token
    )


@given("Get Create Eco News client")
def step_get_create_eco_news_client(context):
    """Get create eco news client"""
    context.access_token = login_user()
    context.client = CreateEcoNewsClient(
        base_url=Config.BASE_API_URL,
        access_token=context.access_token
    )


@when('I send request to add eco news with id "{news_id}" to favorites')
def step_add_to_favorites(context, news_id):
    """Addition to favourites request"""
    context.response = context.client.add_to_favorites_eco_new_by_id(news_id=news_id)


@when('I send request to delete eco news with id "{news_id}"')
def step_delete_news(context, news_id):
    """Deletion of eco new request"""
    context.response = context.client.delete_eco_news_by_id(news_id=news_id)


@when('I send request to delete eco news with id "{news_id}" from favorites')
def step_delete_from_favorites(context, news_id):
    """Deletion from favourites request"""
    context.response = context.client.delete_from_favorites_eco_new_by_id(news_id=news_id)


@when('I send request to dislike eco news with id "{news_id}"')
def step_dislike(context, news_id):
    """Dislike eco new request"""
    context.response = context.client.dislike_eco_news_by_id(news_id=news_id)


@when('I send request to like or unlike eco news with id "{news_id}"')
def step_like_unlike(context, news_id):
    """Like/unlike request"""
    context.response = context.client.like_remove_like_eco_new_by_id(news_id=news_id)


@when('I send request to get summary of eco news with id "{news_id}"')
def step_get_summary(context, news_id):
    """Get eco new summary request"""
    context.response = context.client.get_summary_eco_new(news_id=news_id)


@when('I send request to get recommended eco news with id "{news_id}"')
def step_get_recommended(context, news_id):
    """Get recommended request"""
    context.response = context.client.get_recommended_eco_news(news_id=news_id)


@when('I send PUT request to update eco news with id {news_id} and {data}')
def step_update_with_data(context, news_id, data):
    """Update eco new request"""
    cleaned_data = data.strip().rstrip(':')
    parsed_data = json.loads(cleaned_data)

    context.response = context.client.update_eco_news_by_id(
        news_id=news_id,
        image_file_path=create_test_image(),
        data=parsed_data
    )
    logger.info(f"Response: {context.response.json() if context.response.content else 'Empty'}") # pylint: disable=W1203

@when('I send POST request to create eco news with data:')
def step_create_eco_news(context):
    """Create eco news request"""

    data = json.loads(context.text)

    context.response = context.client.create_eco_news_by_data(
        image_file_path=create_test_image(),
        data=data
    )

@then("the response status code should be {status_code:d}")
def step_status_code(context, status_code):
    """Response status code"""
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"


@then("the response should match schema {schema_name}")
def step_validate_named_schema(context, schema_name):
    """Validation of schema"""
    parsed_data = context.response.json()

    schema_map = {
        "eco_news": one_news_get_by_id_schema,
        "summary": summary_eco_new_schema
    }

    schema = schema_map.get(schema_name)
    assert schema is not None, f"Schema '{schema_name}' not found"

    validate_schema(parsed_data, schema)


@then("each item in response should match schema {schema_name}")
def step_validate_list_schema(context, schema_name):
    """Validation list with schema"""
    parsed_data = context.response.json()

    assert isinstance(parsed_data, list), \
        f"Expected list, got {type(parsed_data)}"

    schema_map = {
        "eco_news": one_news_get_by_id_schema
    }

    schema = schema_map.get(schema_name)

    for item in parsed_data:
        validate_schema(item, schema)


@then('the response message should be {message}')
def step_validate_message(context, message):
    """Validation of message"""
    response = context.response

    try:
        parsed_data = response.json()
        actual_message = parsed_data.get("message")
    except ValueError:
        actual_message = response.text

    assert actual_message is not None, \
        f"No message found in response. Full response: {response.text}"

    assert message in actual_message, \
        f"Expected '{message}', got '{actual_message}'"


@then('the response message for list should be {message}')
def step_validate_message_for_list(context, message):
    """Validation of message in list response"""
    response = context.response

    try:
        parsed_data = response.json()
    except ValueError as e:
        allure.attach(str(e), name="Validation Error",
                      attachment_type=allure.attachment_type.TEXT)
    else:
        assert isinstance(parsed_data, list), \
            f"Expected response to be a list, got {type(parsed_data)}: {parsed_data}"

        messages = [item.get("message") for item in parsed_data if isinstance(item, dict)]

        assert any(msg is not None for msg in messages), \
        f"No 'message' field found in response: {parsed_data}"

        assert any(message in msg for msg in messages if msg), \
        f"Expected '{message}' in one of {messages}"


@then("the response body should be empty")
def step_empty_body(context):
    """Response body is empty"""
    assert not context.response.content, "Expected empty response body"
