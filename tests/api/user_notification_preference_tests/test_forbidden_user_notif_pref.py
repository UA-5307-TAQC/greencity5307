import allure
import pytest

from clients.user_notification_preference_client import UserNotificationPreferenceClient

from data.config import Config

EMAIL_PREF_DATA = [
    "SYSTEM",
    "LIKES",
    "COMMENTS",
    "INVITES",
    "PLACES"
]

EMAIL_PREF_PERIOD_DATA = [
    "IMMEDIATELY",
    "TWICE_A_DAY",
    "DAILY",
    "WEEKLY",
    "MONTHLY",
    "NEVER"
]


@allure.title("Verify 403 Forbidden for ROLE_USER with pref '{email_pref}' and "
              "period '{email_pref_period}'")
@pytest.mark.parametrize(
    "email_pref",
    EMAIL_PREF_DATA
)
@pytest.mark.parametrize(
    "email_pref_period",
    EMAIL_PREF_PERIOD_DATA
)
def test_verify_forbidden_status_code(module_access_token, email_pref, email_pref_period):
    client = UserNotificationPreferenceClient(
        base_url=Config.BASE_USER_API_URL,
        access_token=module_access_token
    )

    response = client.search(
        user_email=Config.USER_EMAIL,
        email_preference=email_pref,
        email_preference_periodicity=email_pref_period
    )

    assert response.status_code == 403, \
        f"Status: {response.status_code}. Response body: {response.text}"

    response_error = response.json().get("error")
    assert response_error == "Forbidden", \
        f"Expected 'Forbidden' error message, got: {response_error}"
