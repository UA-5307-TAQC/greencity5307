"""Test login validation"""
import allure
from clients.base_client import BaseClient


class LoginClient(BaseClient):
    """ Client class specifically for testing the login endpoint,
    independent of the fixture's OwnSecurityClient. """

    def __init__(self, base_url):
        super().__init__(base_url=f"{base_url}")

    @allure.step("Send POST request to login endpoint")
    def login(self, email: str, password: str, project_name: str = "GREENCITY"):
        """Sends credentials to validate the login endpoint behavior."""
        payload = {
            "email": email,
            "password": password,
            "projectName": project_name
        }
        return self._request(
            method="POST",
            endpoint="/signIn",
            json=payload
        )
