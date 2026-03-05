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

    def refresh_token(self, refresh_token: str):
        """Exchanges a refresh token for a new access/refresh token pair.

        Args:
            refresh_token: The refresh token obtained during sign-in.

        Returns:
            Response containing ``accessToken`` and ``refreshToken`` fields.

        Note:
            The GreenCityUser API exposes this as a GET request with the token
            as a path parameter (``/ownSecurity/updateAccessToken/{refreshToken}``).
            This is an existing API contract and cannot be changed on the client side.
            Ensure the refresh token is treated as a secret and not persisted in logs.
        """
        return self._request(
            method="GET",
            endpoint=f"/updateAccessToken/{refresh_token}",
        )
