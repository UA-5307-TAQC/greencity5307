import allure
from jsonschema import validate

from clients.event_comment_client import EventCommentClient

from schemas.event_comment.event_comment_schema import event_comment_schema

from tests.api.event_comment_tests.data import EVENT_ID


@allure.title("Verify that user cannot like or dislike own comments.")
def test_verify_user_cannot_like_dislike_own_event_comment(comment_factory):
    # Precondition: The user is logged in.
    # Post condition: Send a DELETE request to delete the created comment for cleanup.
    client: EventCommentClient = comment_factory.client
    created_comment_id = comment_factory.create_comment(
        event_id=EVENT_ID
    )

    with allure.step("Step 2: "
                     "Send a POST request to like created previously comment."):
        response = client.like_comment(comment_id=created_comment_id)

        # Expected result:
        # Status code is 400. Response body contains an error message
        assert response.status_code == 400, \
            f"POST request failed. Status: {response.status_code}. Response body: {response.text}"

    with allure.step("Step 3: "
                     "Send a GET request to check the likes count of the comment."):
        response = client.get_comment_info(comment_id=created_comment_id)

        # Expected result:
        # Status code is 200. The likes count of the comment remains 0
        assert response.status_code == 200, \
            f"GET request failed. Status: {response.status_code}. Response body: {response.text}"

        response_data = response.json()
        validate(instance=response_data, schema=event_comment_schema)

        assert response_data.get("likes") == 0, \
            f"Likes count was updated. Expected: 0, got: {response_data.get('likes')}"

    with allure.step("Step 4: "
                     "Send a POST request to dislike created previously comment."):
        response = client.dislike_comment(comment_id=created_comment_id)

        # Expected result:
        # Status code is 400. Response body contains an error message
        assert response.status_code == 400, \
            f"POST request failed. Status: {response.status_code}. Response body: {response.text}"

    with allure.step("Step 5: "
                     "Send a GET request to check the dislikes count of the comment."):
        response = client.get_comment_info(comment_id=created_comment_id)

        # Expected result:
        # Status code is 200. The dislikes count of the comment remains 0
        assert response.status_code == 200, \
            f"GET request failed. Status: {response.status_code}. Response body: {response.text}"

        response_data = response.json()
        validate(instance=response_data, schema=event_comment_schema)

        assert response_data.get("dislikes") == 0, \
            f"Likes count was updated. Expected: 0, got: {response_data.get('dislikes')}"
