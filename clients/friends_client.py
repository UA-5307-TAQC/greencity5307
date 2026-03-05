"""Client for interacting with Friends API."""

import allure
from requests import Response
from clients.base_client import BaseClient


class FriendsClient(BaseClient):
    """Client for interacting with Friends API."""

    def __init__(self, base_url, access_token=None):
        """Init FriendsClient."""
        super().__init__(base_url=f"{base_url}/friends", access_token=access_token)

    @allure.step("Get list of all friends")
    def get_all_friends(self, page: int = 0, size: int = 10) -> Response:
        """Get all friends list."""

        params = {
            "page": page,
            "size": size
        }

        return self._request("GET", "", params=params)

    @allure.step("Get mutual friends.")
    def get_mutual_friends(self, friend_id: int, page: int = 0, size: int = 10) -> Response:
        """Fetch mutual friends."""
        params = {
            "friendId": friend_id,
            "page": page,
            "size": size
        }
        return self._request("GET", "/mutual-friends", params=params)
