"""Get all social network images forbidden verification"""
import allure

from clients.social_network_images_client import SocialNetworkImagesClient
from data.config import Config


@allure.feature("Social Network Images")
@allure.story("Get all images - forbidden")
@allure.title("Verify getting social network images is forbidden for user")
def test_get_all_social_network_images_forbidden(access_token):
    """Test that authorized user without proper role gets 403"""
    client = SocialNetworkImagesClient(
        base_url=Config.BASE_USER_API_URL,
        access_token=access_token
    )

    response = client.get_all_social_network_images()

    assert response.status_code == 403, (
        f"Expected status code 403, but got {response.status_code}. "
        f"Response: {response.text}"
    )
    assert response.json()["error"] == "Forbidden"