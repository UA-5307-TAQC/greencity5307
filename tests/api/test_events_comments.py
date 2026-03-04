"""API tests for the Events comments functionality."""
import allure

from clients.event_comment_client import EventCommentClient

from data.config import Config

EVENT_ID = 31
TEXT = "Some text to backend from AQA."


@allure.title("Verify that an unauthorized user cannot leave a comment")
def test_unauthorized_user_cannot_leave_comment():
    """Testcase that an anonymous user cannot post a comment on an event."""
    client = EventCommentClient(base_url=Config.BASE_API_URL)

    with allure.step("Step 1: Attempt to send a POST request without an Authorization token."):
        response = client.create_comment(
            event_id=EVENT_ID,
            text=TEXT,
        )
        assert response.status_code == 401, f"Error: {response.status_code}"


@allure.title("Verify that an authorized user can successfully leave and delete a comment.")
def test_authorized_user_can_leave_comment(access_token):
    """Testcase that an authorized user can successfully post a comment and delete it."""
    # Precondition: The user is logged in.
    client = EventCommentClient(base_url=Config.BASE_API_URL, access_token=access_token)

    with allure.step("Step 1: "
                     "Get the initial count of comments on the target event page."):
        response = client.get_comments_count(event_id=EVENT_ID)

        # Expected result: Successful response and count of comments.
        assert response.status_code == 200, f"Error: {response.status_code}"
        count_before_creation = int(response.text)

    with allure.step("Step 2: "
                     "Send a POST request with valid credentials to leave a new comment."):
        response = client.create_comment(
            event_id=EVENT_ID,
            text=TEXT
        )

        # Expected result: Successful response and posted comment text matches with actual.
        assert response.status_code == 201, f"Error: {response.status_code}"

        posted_comment_text = response.json()["text"]
        comment_id = response.json()["id"]
        assert posted_comment_text == TEXT, \
            f"Comments do not match. Expected: {TEXT}, got: {posted_comment_text}"

    with allure.step("Step 3: "
                     "Fetch the updated comments count and verify it incremented by one"):
        response = client.get_comments_count(event_id=EVENT_ID)
        count_after_creation = int(response.text)

        # Expected result: Successful response and count of comments increments by one.
        assert response.status_code == 200, f"Error: {response.status_code}"
        assert count_after_creation == count_before_creation + 1, \
            (f"Comments count does not match. Expected: {count_before_creation + 1},"
             f"got: {count_after_creation}")

    with allure.step("Step 4: "
                     "Send a DELETE request and verify that the comment is deleted."):
        response = client.delete_comment(comment_id=comment_id)

        # Expected result: Successful response.
        assert response.status_code == 200, f"Error: {response.status_code}"

    with allure.step("Step 5: "
                     "Fetch the updated comments and verify it decremented by one."):
        response = client.get_comments_count(event_id=EVENT_ID)

        # Expected result: Successful response and count of comments decrements by one.
        assert response.status_code == 200, f"Error: {response.status_code}"

        comments_count_after_deletion = int(response.text)
        assert comments_count_after_deletion == count_after_creation - 1, \
            (f"Comments count does not match. Expected: {count_after_creation - 1},"
             f"got: {comments_count_after_deletion}")
