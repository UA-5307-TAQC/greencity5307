"""GreenCity User API behave steps."""

import json

import allure
from behave import given, when, then
from jsonschema import validate

from clients.greencity_user_api.user_client import UserClient
from schemas.greencity_user_api.user.pageable_dto_user_for_list_schema import \
    pageable_dto_user_for_list_schema
from schemas.greencity_user_api.user.user_update_dto_schema import \
    user_update_dto_schema
from utils.logger import logger


# =========================
# GIVEN STEPS
# =========================

@given("created UserClient")
def step_create_user_client(context):
    """Create UserClient instance using authentication token stored in context."""
    context.client = UserClient(access_token=context.auth_token)


# =========================
# WHEN STEPS
# =========================

@when("I send request to filter user by page with filters: {query} and {body}")
def step_request_filter_all_user_by_search_criteria(context, query, body):
    """
    Send request to filter users by page with query parameters and request body.

    Args:
        query (str): JSON string containing query parameters.
        body (str): JSON string containing request body filters.
    """
    query_dict = json.loads(query)
    body_dict = json.loads(body)

    context.response = context.client.filter_all_user_by_search_criteria(
        **query_dict,
        **body_dict
    )
    logger.info("STATUS CODE: %s", context.response.status_code)


@when("I send request to get user dto by principal")
def step_request_user_dto_by_principal(context):
    """Send request to retrieve current user DTO using access token (principal-based request)."""
    context.response = context.client.get_user_dto_by_principal_from_access_token()
    logger.info("STATUS CODE: %s", context.response.status_code)


@when(
    "I send request to update user by user management with payload: {payload}")
def step_update_user_by_management(context, payload):
    """
    Send request to update user via user management endpoint.

    Args:
        payload (str): JSON string containing user update data.
    """
    payload_dict = json.loads(payload)

    context.response = context.client.update_user_by_user_management(
        **payload_dict)
    logger.info("STATUS CODE: %s", context.response.status_code)


@when("I send request to update user with payload: {payload}")
def step_update_user(context, payload):
    """
    Send request to update current authenticated user profile.

    Args:
        payload (str): JSON string containing user update data.
    """
    payload_dict = json.loads(payload)

    context.response = context.client.update_user(**payload_dict)
    logger.info("STATUS CODE: %s", context.response.status_code)


# =========================
# THEN STEPS
# =========================

@then("validate schema for filter user by page with filters if successful")
def step_filter_all_user_by_search_criteria_schema_validation(context):
    """
    Validate response schema for successful user filtering request (HTTP 200 only).
    """
    if context.response.status_code == 200:
        with allure.step("Validate successful response"):
            parsed_data = context.response.json()
            logger.info("RESPONSE DATA: %s", parsed_data)

            validate(instance=parsed_data,
                     schema=pageable_dto_user_for_list_schema)


@then("validate schema for user dto by principal")
def step_user_dto_by_principal_schema_validation(context):
    """
    Validate response schema for user DTO returned by principal endpoint (HTTP 200 only).
    """
    if context.response.status_code == 200:
        parsed_data = context.response.json()
        logger.info("RESPONSE DATA: %s", parsed_data)

        validate(instance=parsed_data, schema=user_update_dto_schema)


@then("validate if user access is forbidden")
def step_validate_user_403_error(context):
    """
    Validate that response contains 403 Forbidden error with correct message.
    """
    if context.response.status_code == 403:
        parsed_error = context.response.json()
        logger.info('Error: %s', parsed_error)
        assert parsed_error[
                   'error'] == "Forbidden", "Wrong authorization error message"


@then("validate if user is unauthorised")
def step_validate_user_401_error(context):
    """
    Validate that response contains 401 Unauthorized error with correct message.
    """
    if context.response.status_code == 401:
        parsed_error = context.response.json()
        logger.info('Error: %s', parsed_error)
        assert parsed_error[
                   'error'] == "Unauthorized", "Wrong unauthorized error message"


@then("user response status code should be successful or forbidden")
def step_successful_or_forbidden(context):
    """
    Assert that response status code is either 200 (success) or 403 (forbidden).
    """
    assert context.response.status_code in (200, 403), (
        f"Unexpected status code: {context.response.status_code}"
    )


@then("user response status code should be unauthorized")
def step_unauthorised(context):
    """
    Assert that response status code is 401 Unauthorized.
    """
    assert context.response.status_code == 401, (
        f"Unexpected status code: {context.response.status_code}"
    )
