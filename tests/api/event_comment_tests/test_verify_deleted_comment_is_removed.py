import allure
from jsonschema import validate

from schemas.event_comment.event_page_comment_schema import event_comments_list_schema

from clients.event_comment_client import EventCommentClient

from tests.api.event_comment_tests.data import EVENT_ID


@allure.title("Verify deleted event comment is removed from the active comments list")
def test_verify_deleted_comment_is_removed_from_comments_list(comment_factory):
    # Precondition: The user is logged in.
    client: EventCommentClient = comment_factory.client
    created_comment_id = comment_factory.create_comment(
        event_id=EVENT_ID
    )

    with allure.step("Step 2: "
                     "Send a GET request to get the list of active comments"):
        response = client.get_comments_from_event(event_id=EVENT_ID)
        response_data = response.json()

        # Expected result:
        # Status Code is 200. The created comment is present in the returned list of comments
        assert response.status_code == 200, \
            f"Error. Status code: {response.status_code}. Body: {response.text}"

        validate(instance=response_data, schema=event_comments_list_schema)

        list_of_comments = response_data.get("page")
        is_comment_present = any(
            [comment.get("id") == created_comment_id for comment in list_of_comments]
        )
        assert is_comment_present, \
            f"Created comment is not in the list. Got list of comments: {list_of_comments}"

    with allure.step("Step 3: "
                     "Send a DELETE request to delete the comment"):
        response = client.delete_comment(comment_id=created_comment_id)

        # Expected result:
        # HTTP Status Code is 200
        assert response.status_code == 200, \
            f"Deletion failed. Status code: {response.status_code}, body: {response.text}"

    with allure.step("Step 4: "
                     "Send a GET request to get the list of active comments"):
        response = client.get_comments_from_event(event_id=EVENT_ID)
        response_data = response.json()

        # Expected result:
        # HTTP Status Code is 200. The deleted comment is not present in the returned list of comments
        assert response.status_code == 200, \
            f"Error. Status code: {response.status_code}. Body: {response.text}"

        validate(instance=response_data, schema=event_comments_list_schema)

        list_of_comments_after_deletion = response_data.get("page")
        is_comment_present = any(
            [comment.get("id") == created_comment_id for comment in list_of_comments_after_deletion]
        )
        assert not is_comment_present, \
            f"Created comment is in the list. Got list of comments: {list_of_comments_after_deletion}"
