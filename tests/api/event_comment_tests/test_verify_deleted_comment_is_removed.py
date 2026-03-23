import allure
from jsonschema import validate

from schemas.event_comment.event_comment_schema import event_comment_schema

from clients.event_comment_client import EventCommentClient

from data.config import Config

from tests.api.event_comment_tests.data import EVENT_ID, TEXT

from utils.logger import logger


@allure.title("Verify deleted event comment is removed from the active comments list")
def test_verify_deleted_comment_is_removed_from_comments_list(access_token):
    with allure.step("Precondition: "
                     "The user is logged in."):
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

        assert response.status_code == 201

        response_data = response.json()
        validate(instance=response_data, schema=event_comment_schema)

        assert response_data.get("text") == TEXT, \
            f"Comments do not match. Expected: {TEXT}, got: {response_data.get("text")}"

        created_comment_id = response_data.get("id")

    with allure.step("Step 2: "
                     "Send a GET request to get the list of active comments"):
        response = client.get_comments_from_event(event_id=EVENT_ID)
        response_data = response.json()

        # Expected result:
        # Status Code is 200. The created comment is present in the returned list of comments
        assert response.status_code == 200, \
            f"Error. Status code: {response.status_code}. Body: {response.text}"

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

        list_of_comments_after_deletion = response_data.get("page")
        is_comment_present = any(
            [comment.get("id") == created_comment_id for comment in list_of_comments_after_deletion]
        )
        assert not is_comment_present, \
            f"Created comment is in the list. Got list of comments: {list_of_comments_after_deletion}"
