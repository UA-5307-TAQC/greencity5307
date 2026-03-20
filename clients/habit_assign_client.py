"""Client for interacting with the Habit API, extending BaseClient for common functionality."""

from requests import Response
from clients.base_client import BaseClient


class HabitAssignClient(BaseClient):
    """Client for interacting with the Habit API,
     extending BaseClient for common functionality."""


    def __init__(self, base_url, access_token=None):
        super().__init__(base_url=f"{base_url}/habit/assign", access_token=access_token)


    def assign_habit_with_default_properties(self, habit_id: int) -> Response:
        """Assign habit with default properties"""

        return self._request(
            method="POST",
            endpoint=f"/{habit_id}"
        )


    def get_all_assigned_habits(self, lang: str = "en-GB") -> Response:
        """Find all assigned habits"""

        params = {
            "lang": lang,
        }

        return self._request(
            method="GET",
            endpoint="/allForCurrentUser",
            params=params
        )


    def delete_habit_assign(self, habit_assign_id: int) -> Response:
        """Delete assigned habit"""

        return self._request(
            method="DELETE",
            endpoint=f"/delete/{habit_assign_id}"
        )
