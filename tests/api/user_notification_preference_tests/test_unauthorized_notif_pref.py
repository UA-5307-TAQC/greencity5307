import allure

from clients.user_notification_preference_client import UserNotificationPreferenceClient

from data.config import Config


@allure.title("Verify 401 Unauthorized on preference search without auth token")
def test_verify_unauthorized_status_code():
    client = UserNotificationPreferenceClient(
        base_url=Config.BASE_USER_API_URL
    )

    response = client.search(
        user_email=Config.USER_EMAIL,
        email_preference="SYSTEM",
        email_preference_periodicity="IMMEDIATELY"
    )

    assert response.status_code == 401, \
        f"Status: {response.status_code}. Response body: {response.text}"

    response_error = response.json().get("error")
    assert response_error == "Unauthorized", \
        f"Expected 'Unauthorized' error message, got: {response_error}"
