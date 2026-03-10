"""Client for interacting with the Email API."""

import allure
from requests import Response
from clients.base_client import BaseClient


class EmailClient(BaseClient):
    """Client for interacting with the Email API."""

    def __init__(self, base_url, access_token=None):
        super().__init__(base_url=f"{base_url}/email", access_token=access_token)

    @allure.step("Send Telegram feedback email")
    def send_telegram_feedback(self, payload: dict) -> Response:
        """Send Telegram user feedback to customer email."""
        return self._request("POST", "/telegram-feedback", json=payload)

    @allure.step("Send user violation email.")
    def send_user_violation(self, payload: dict) -> Response:
        """Send user violation email."""
        return self._request("POST", "/sendUserViolation", json=payload)

    @allure.step("Send report email")
    def send_report(self, payload: dict) -> Response:
        """Send report email to subscribers with new places."""
        return self._request("POST", "/sendReport", json=payload)

    @allure.step("Send reason of deactivation.")
    def send_reason_of_deactivation(self, payload: dict) -> Response:
        """Send reason of deactivation."""
        return self._request("POST", "/sendReasonOfDeactivation", json=payload)

    @allure.step("Send place status change.")
    def send_place_status_change(self, payload: dict) -> Response:
        """Send place status change."""
        return self._request("POST", "/sendPlaceStatusChange", json=payload)

    @allure.step("Send message of activation user account.")
    def send_message_of_account_activation(self, payload: dict) -> Response:
        """Send message of user account activation."""
        return self._request("POST", "/sendMessageOfActivation", json=payload)

    @allure.step("Send interesting eco news email.")
    def send_interesting_eco_news(self, payload: dict) -> Response:
        """Send interesting eco news email."""
        return self._request("POST", "/sendInterestingEcoNews", json=payload)

    @allure.step("Send email notification about habit.")
    def send_habit_notification(self, payload: dict) -> Response:
        """Send habit notification."""
        return self._request("POST", "/sendHabitNotification", json=payload)

    @allure.step("Send scheduled notifications via email.")
    def send_scheduled_notifications(self, payload: dict) -> Response:
        """Send scheduled notifications via email."""
        return self._request("POST", "/scheduled/notifications", json=payload)

    @allure.step("Send green office notifications via email.")
    def send_green_office_notifications(self, payload: dict) -> Response:
        """Send green office notifications via email."""
        return self._request("POST", "/greenoffice/notification", json=payload)
