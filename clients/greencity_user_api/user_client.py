"""Client for interacting with the Eco News API, extending BaseClient for common functionality."""
import allure
from requests import Response

from clients.base_client import BaseClient
from data.config import Config
from utils.logger import logger


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

    @allure.step(
        "Update user by UserManagement, request object: email={email}, "
        "role={role}, userStatus={userStatus}, name={name},")
    # pylint: disable=invalid-name
    def update_user_by_user_management(self, email: str,
                                       role: str,
                                       userStatus: str,
                                       name: str = None) -> Response:
        """Update user using UserManagement API."""

        payload = {
            "email": email,
            "role": role,
            "userStatus": userStatus,
        }

        if name is not None:
            payload["name"] = name

        return self._request(method="PUT", json=payload)

    @allure.step("Update user")
    # pylint: disable=invalid-name
    def update_user(self, emailNotification: str,
                    name: str = None) -> Response:
        """Update user using UserManagement API."""

        payload = {
            "email": emailNotification,
        }

        if name is not None:
            payload["name"] = name

        return self._request(method="PATCH", json=payload)

    @allure.step(
        "Find eco news by page with filters: page={page}, size={size}, "
        "sort={sort}")
    # pylint: disable=invalid-name
    def filter_all_user_by_search_criteria(self,
                                           page: int = 0,
                                           size: int = 5,
                                           sort: str = "asc",
                                           searchReg: str = None) -> Response:
        """Find eco news by page with optional filters and sorting."""
        params = {
            "page": page,
            "size": size,
            "sort": sort,
        }
        json = {}
        if searchReg:
            json["searchReg"] = searchReg

        logger.info("Find eco news by page with params: %s", params)
        logger.info("Find eco news by page with json: %s", json)

        return self._request("POST", 'filter', params=params, json=json)
