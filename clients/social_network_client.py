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


    def delete_social_network_by_id(self, network_id):
        """Delete social network by id"""

        params = network_id

        return self._request(
            method="DELETE",
            endpoint="",
            params=params
        )
