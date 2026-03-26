"""Client for interacting with the Eco News API, extending BaseClient for common functionality."""
import allure
from requests import Response

from clients.base_client import BaseClient
from data.config import Config


class UserClient(BaseClient):
    """Client for interacting with the User API,
     extending BaseClient for common functionality."""

    def __init__(self, access_token=None):
        """Client for interacting with the User API,
        extending BaseClient for common functionality."""
        super().__init__(base_url=f"{Config.BASE_USER_API_URL}/user",
                         access_token=access_token)

    @allure.step("Get User dto by principal (email) from access token")
    def get_user_dto_by_principal_from_access_token(self) -> Response:
        """Find one eco news by id with optional filters."""

        return self._request("GET")
