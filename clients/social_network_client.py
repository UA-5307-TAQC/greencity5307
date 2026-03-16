"""Client for social networks requests validation"""
from clients.base_client import BaseClient


class SocialNetworkClient(BaseClient):
    """Client for social networks requests validation"""

    def __init__(self, base_url, access_token=None):
        """Initializes the OwnSecurityClient with the specific base URL
        for authentication endpoints."""
        super().__init__(
            base_url=f"{base_url}/social-networks",
            access_token=access_token
        )

    def get_image_social_networks(self, url: str):
        """Get valid image path for social networks request"""

        params = {
            "url": url
        }

        return self._request(
            method="GET",
            endpoint="/image",
            params=params
        )
