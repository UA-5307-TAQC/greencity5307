"""API tests for the Events comments functionality."""
import json

import requests
import allure

EVENT_ID = 31
TARGET_URL = f"https://greencity.greencity.cx.ua/events/{EVENT_ID}/comments"


@allure.title("Verify that an unauthorized user cannot leave a comment")
def test_unauthorized_user_cannot_leave_comment():
    """Testcase that an anonymous user cannot post a comment on an event."""
    payload = {
        "text": "Some text to backend from AQA.",
        "parentCommentId": 0
    }

    with allure.step("Attempt to send a POST request without an Authorization token."):
        response = requests.post(TARGET_URL, json=payload)

        # Expected result: Unsuccessful response with 401 status code.
        assert response.status_code == 401, "Unauthorized user can leave a comment."


@allure.title("Verify that an authorized user can successfully leave a comment")
def test_authorized_user_can_leave_comment(auth_headers):
    """Testcase that an authorized user can successfully post a comment and update the state."""
    # Precondition: The user is logged in.
    with allure.step("Get the initial count of comments on the target event page."):
        response = requests.get(url=f"{TARGET_URL}/count", headers=auth_headers)
        comments_count_before = int(response.text)

        # Expected result: Successful response and count of comments.
        assert response.status_code == 200, f"Error: {response.status_code}"

    with allure.step("Send a POST request with valid credentials to leave a new comment."):
        payload = {
            "text": "Some text to backend from AQA.",
            "parentCommentId": 0
        }
        files = {
            "request": (None, json.dumps(payload)),
        }
        response = requests.post(TARGET_URL, headers=auth_headers, files=files)

        # Expected result: Successful response and posted comment text matches with actual.
        assert response.status_code == 201, f"Error: {response.status_code}"

        posted_comment_text = response.json()["text"]
        actual_comment_text = payload["text"]
        assert posted_comment_text == actual_comment_text, \
            f"Comments do not match. Expected: {actual_comment_text}, got: {posted_comment_text}"

    with allure.step("Fetch the updated comments count and verify it incremented by one"):
        response = requests.get(url=f"{TARGET_URL}/count", headers=auth_headers)
        comments_count_after = int(response.text)

        # Expected result: Successful response and count of comments increments by one.
        assert response.status_code == 200, f"Error: {response.status_code}"
        assert comments_count_after == comments_count_before + 1, \
            f"Comments count does not match."
