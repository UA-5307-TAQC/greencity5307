import allure
from pytest import fixture
from jsonschema import validate

from schemas.event_comment.event_comment_schema import event_comment_schema

from clients.event_comment_client import EventCommentClient

from data.config import Config

from tests.api.event_comment_tests.data import EVENT_ID, TEXT


@fixture
def created_test_comment_and_client(access_token):
    """Fixture that logs in user as precondition, creates an event comment
    and deletes it as post condition."""
    with allure.step("Precondition: The user is logged in."):
        client = EventCommentClient(
            base_url=Config.BASE_API_URL,
            access_token=access_token
        )

    with allure.step("Step 1: "
                     "Send a POST request to create a new comment on the target event page."):
        response = client.create_comment(
            event_id=EVENT_ID,
            text=TEXT
        )

        assert response.status_code == 200, \
            (f"Creation of comment was failed. "
             f"Status code: {response.status_code}, "
             f"body: {response.text}")

        response_data = response.json()
        validate(instance=response_data, schema=event_comment_schema)

        assert response_data.get("text") == TEXT, \
            f"Comments do not match. Expected: {TEXT}, got: {response_data.get("text")}"

        created_comment_id = response_data.get("id")

    yield created_comment_id, client

    with allure.step("Post condition: "
                     "Send a DELETE request to delete the created comment for cleanup."):
        response = client.delete_comment(comment_id=created_comment_id)
        status_code = response.status_code
        body = response.text

        assert status_code == 200, \
            f"Failed to delete the created comment. Status: {status_code}, body: {body}"
