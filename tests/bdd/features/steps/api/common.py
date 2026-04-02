# pylint: disable=not-callable, unused-argument
"""
.. module:: common
    :platform: Unix
    :synopsis: """
import json
from collections import defaultdict

import allure
from behave import given, then
from jsonschema import Draft7Validator

from clients.own_security_client import OwnSecurityClient
from data.config import Config


def validate_json_schema(schema, data):
    """Reusable JSON schema validator with Allure reporting."""
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
                report_lines.append(
                    f"{i}. [{path}] -> {err.message} (Actual: {err.instance})")

            allure.attach(
                "\n".join(report_lines),
                name=f"JSON Schema Mismatch: Record #{index}",
                attachment_type=allure.attachment_type.TEXT
            )

        raise AssertionError(
            f"JSON validation failed. Found {len(errors)} total schema errors.")


@given('the user is authorized')
def login_user(context):
    """Function that logs in the user and returns auth token."""
    client = OwnSecurityClient(Config.BASE_USER_API_URL)
    response = client.sign_in(
        email=Config.USER_EMAIL,
        password=Config.USER_PASSWORD
    )

    assert response.status_code == 200, \
        f"Login failed. Status: {response.status_code}. Response body: {response.text}"

    token = response.json().get("accessToken")
    assert token, \
        f"Login response does not contain access token. Response body: {response.text}"

    context.access_token = token


@given("I have invalid access token")
def step_invalid_token(context):
    """Create an invalid access token"""
    context.access_token = "not_access_token"


@then('the response JSON should match the schema')
def validate_json(context):
    """Validate response json schema"""
    validate_json_schema(context.schema, context.response.json())


@then('the response status code should be {expected_code:d}')
def check_response_code(context, expected_code):
    """Check response status code"""
    actual_code = context.response.status_code
    assert actual_code == expected_code, f"Code is {actual_code}"


@then("the response body should be empty")
def step_empty_body(context):
    """Response body is empty"""
    content = context.response.text.strip()
    assert content == "", f"Content is empty. Response body: {content}"


@then("validate if bad request")
def step_validate_bad_request(context):
    """Assert that the response status code is 400 Bad Request."""
    assert context.response.status_code == 400, "Wrong bad request response"


@then("validate if unauthorised")
def step_validate_unauthorised(context):
    """Assert that the response status code is 401 Unauthorized."""
    assert context.response.status_code == 401, "Wrong unauthorised response"


@then("response status code should be {status:d}")
def step_status(context, status):
    """
    Assert that the response status code matches the expected value.

    Args:
        status (int): Expected HTTP status code.
    """
    assert context.response.status_code == status, (
        f"Expected {status}, got {context.response.status_code}"
    )
