"""Module that contains client for interacting with the Own Security API,
extending BaseClient for common functionality."""
from clients.base_client import BaseClient


class OwnSecurityClient(BaseClient):
    """Client class for interacting with the Own Security API,
    extending BaseClient for common functionality."""
    def __init__(self, access_token=None):
        """Initializes the OwnSecurityClient with the specific base URL
        for authentication endpoints."""
        super().__init__(
            base_url="https://greencity-user.greencity.cx.ua/ownSecurity",
            access_token=access_token
        )

    def sign_in(self, email: str, password: str):
        """Authenticates a user with the provided credentials.
        Returns the response containing the user data and access token."""
        payload = {
            "email": email,
            "password": password,
            "projectName": "GREENCITY"
        }
        return self._request(
            method="POST",
            endpoint="/signIn",
            json=payload
        )
