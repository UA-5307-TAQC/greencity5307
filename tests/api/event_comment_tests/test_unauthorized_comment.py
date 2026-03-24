import allure

from clients.event_comment_client import EventCommentClient

from data.config import Config

from tests.api.event_comment_tests.data import EVENT_ID, TEXT


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
