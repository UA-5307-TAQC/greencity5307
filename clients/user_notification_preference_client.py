"""Module that contains client for interacting with
the User Notification Preference Controller API,
extending BaseClient for common functionality."""
from clients.base_client import BaseClient


class UserNotificationPreferenceClient(BaseClient):
    """Client class for interacting with the
    User Notification Preference Controller API,
    extending BaseClient for common functionality."""
    def __init__(self, base_url, access_token=None):
        super().__init__(
            base_url=f"{base_url}/user-notification-preference",
            access_token=access_token
        )

    def search(
            self,
            user_email,
            email_preference,
            email_preference_periodicity
    ):
        """Checks if a user notification preference exists for
        the given email, preference, and periodicity."""
        payload = {
            "userEmail": user_email,
            "emailPreference": email_preference,
            "emailPreferencePeriodicity": email_preference_periodicity
        }

        return self._request(
            method="POST",
            endpoint="/search",
            json=payload
        )
