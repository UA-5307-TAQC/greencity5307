"""Module that contains client for interacting with the Own Security API,
extending BaseClient for common functionality."""
from clients.base_client import BaseClient


class OwnSecurityClient(BaseClient):
    """Client class for interacting with the Own Security API,
    extending BaseClient for common functionality."""
    def __init__(self, base_url, access_token=None):
        """Initializes the OwnSecurityClient with the specific base URL
        for authentication endpoints."""
        super().__init__(
            base_url=f"{base_url}/ownSecurity",
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

    def change_password(self,password,confirm_password):
        """Change the password of the user."""
        payload ={
            "password":password,
            "confirmPassword":confirm_password
        }
        return self._request(
            method="PUT",
            endpoint="/changePassword",
            json=payload
        )
