import allure
import pytest

from jsonschema import validate

from clients.event_comment_client import EventCommentClient

from schemas.event_comment.event_comment_schema import event_comment_schema

from tests.api.event_comment_tests.data import EVENT_ID, TEXT


@pytest.mark.xfail(reason="Bug: Backend saves PATCH payload with JSON literal quotes included", strict=True)
@allure.title("Verify user can successfully update their own event comment")
def test_verify_user_can_update_own_event_comment(comment_factory):
    # Precondition: The user is logged in.
    # Post condition: Send a DELETE request to delete the created comment for cleanup.
    client: EventCommentClient = comment_factory.client
    created_comment_id = comment_factory.create_comment(
        event_id=EVENT_ID
    )

    with allure.step("Step 2: "
                     "Send a PATCH request to update the text "
                     "of the previously created comment."):
        response = client.update_comment(
            comment_id=created_comment_id,
            new_text=TEXT
        )

        # Expected result:
        # HTTP Status Code is 200.
        assert response.status_code == 200, \
            (f"PATCH request failed. "
             f"Status code: {response.status_code} "
             f"Body: {response.text}")

    with allure.step("Step 3: "
                     "Send a GET request to retrieve the specific "
                     "comment's information to verify the update."):
        response = client.get_comment_info(comment_id=created_comment_id)
        response_data = response.json()

        # Expected result:
        # HTTP Status Code is 200. The text field in the response strictly matches the updated text.
        assert response.status_code == 200, \
            (f"GET request failed. "
             f"Status code: {response.status_code} "
             f"Body: {response.text}")

        validate(instance=response_data, schema=event_comment_schema)

        assert response_data.get("text") == TEXT, \
            (f"Updating the comment's text failed. "
             f"Expected text: {TEXT}, "
             f"got: {response_data.get("text")}. "
             f"Body: {response.text}")
