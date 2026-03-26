"""Client for social network images requests"""
from clients.base_client import BaseClient


class SocialNetworkImagesClient(BaseClient):
    """Client for social network images requests"""

    def __init__(self, base_url, access_token=None):
        """Initialize social network images client"""
        super().__init__(
            base_url=f"{base_url}/management/socialnetworkimages",
            access_token=access_token
        )

    def delete_social_network_image(self, image_id):
        """Delete social network image"""
        return self._request(
            method="DELETE",
            endpoint="/delete",
            params={"id": image_id}
        )
    def update_social_network_image(self, body):
        """Update social network image"""
        return self._request(
            method="PUT",
            endpoint="",
            json=body
        )
    def create_social_network_image(self, body):
        """Create social network image"""
        return self._request(
            method="POST",
            endpoint="/",
            json=body
        )
