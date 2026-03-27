"""Eco news api feature steps"""
import tempfile

import allure
from PIL import Image
from behave import given, when, then
from jsonschema import validate, ValidationError

from clients.eco_new_client import EcoNewClient
from data.config import Config
from schemas.news.eco_news_response_schema import eco_news_response_schema
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


@given('Get EcoNewsClient')
def step_get_eco_news_client(context):
    """ Get EcoNewsClient """

    context.client = EcoNewClient(
        base_url=Config.BASE_API_URL,
        access_token=getattr(context, "access_token", None)
    )


@when(
    'the client sends a request to get eco news with id {news_id} and language {lang}')
def step_get_by_id(context, news_id, lang):
    """Get one eco news by id"""
    context.news_id = news_id
    context.response = context.client.find_eco_news_by_id(news_id=news_id,
                                                          lang=lang)


@when("the client sends a request to retrieve eco news with parameters")
def step_get_eco_news(context):
    """
    Sends a request to retrieve eco news using query parameters from a Gherkin table.

    The step parses input values from the context.table and converts them into
    appropriate Python types before sending the request:
        - "null" → None
        - "true"/"false" → boolean
        - "[a, b]" → list of strings
        - numeric strings → integers
        - otherwise → string

    The resulting parameters are passed as keyword arguments to the eco news
    pagination endpoint.
    """
    params = {}

    for row in context.table:
        for key in row.headings:
            value = row[key]

            if value == "null":
                params[key] = None

            elif value.lower() in ["true", "false"]:
                params[key] = value.lower() == "true"

            elif value.startswith("[") and value.endswith("]"):
                # [news, education]
                inner = value[1:-1].strip()
                params[key] = [x.strip() for x in inner.split(",") if
                               x.strip()]

            elif value.lstrip("-").isdigit():
                params[key] = int(value)

            else:
                params[key] = value

    context.response = context.client.find_eco_news_by_page(**params)


@when('I send request to add eco news with id "{news_id}" to favorites')
def step_add_to_favorites(context, news_id):
    """Addition to favourites request"""
    context.response = context.client.add_to_favorites_eco_new_by_id(
        news_id=news_id)


@when('I send request to delete eco news with id "{news_id}"')
def step_delete_news(context, news_id):
    """Deletion of eco new request"""
    context.response = context.client.delete_eco_news_by_id(news_id=news_id)


@when('I send request to delete eco news with id "{news_id}" from favorites')
def step_delete_from_favorites(context, news_id):
    """Deletion from favourites request"""
    context.response = context.client.delete_from_favorites_eco_new_by_id(
        news_id=news_id)


@when('I send request to dislike eco news with id "{news_id}"')
def step_dislike(context, news_id):
    """Dislike eco new request"""
    context.response = context.client.dislike_eco_news_by_id(news_id=news_id)


@when('I send request to like or unlike eco news with id "{news_id}"')
def step_like_unlike(context, news_id):
    """Like/unlike request"""
    context.response = context.client.like_remove_like_eco_new_by_id(
        news_id=news_id)


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
    context.response = context.client.update_eco_news_by_id(
        news_id=news_id,
        image_file_path=create_test_image(),
        data=data
    )
    logger.info(
        "Response: %s",
        context.response.json() if context.response.content else "Empty"
    )


@then("the response status code should be {status_code:d}")
def step_status_code(context, status_code):
    """Response status code"""
    assert context.response.status_code == status_code, \
        f"Expected {status_code}, got {context.response.status_code}"


@then("the response should match schema {schema_name}")
def step_validate_named_schema(context, schema_name):
    """Validation of schema"""
    if context.response.status_code == 200:
        parsed_data = context.response.json()

        schema_map = {
            "one_eco_news": one_news_get_by_id_schema,
            "summary": summary_eco_new_schema,
            "page": eco_news_response_schema,
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
    parsed_data = context.response.json()
    assert parsed_data["message"] == message, \
        f"Expected '{message}', got '{parsed_data['message']}'"


@then("if the status code is 400 validate message")
def step_validate_400_message(context):
    """
    Validate error message for 400 Bad Request if applicable.
    """
    if context.response.status_code == 400:
        expected_message = context.text.strip()
        actual_message = context.response.json().get("message")

        logger.info("EXPECTED: %s", expected_message)
        logger.info("ACTUAL: %s", actual_message)

        assert actual_message == expected_message, (
            f"Expected '{expected_message}', got '{actual_message}'"
        )


@then("if the status code is 404 validate message")
def step_validate_404_message(context):
    """
    Validate error message for 404 Not Found if applicable.
    """
    if context.response.status_code == 404:
        expected_message = context.text.replace("<news_id>",
                                                str(context.news_id)).strip()
        actual_message = context.response.json().get("message")

        logger.info("EXPECTED: %s", expected_message)
        logger.info("ACTUAL: %s", actual_message)

        assert actual_message == expected_message, (
            f"Expected '{expected_message}', got '{actual_message}'"
        )


@then("handle other eco news find by id responses")
def step_handle_find_by_id_other_responses(context):
    """Validate allowed response codes for eco news by id endpoint"""
    assert context.response.status_code in (200, 400, 404), (
        f"Unexpected status code: {context.response.status_code}"
    )
