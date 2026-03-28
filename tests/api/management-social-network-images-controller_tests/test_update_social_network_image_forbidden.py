"""Social network image update forbidden verification"""
# pylint: disable=duplicate-code
import allure
import pytest

from clients.social_network_images_client import SocialNetworkImagesClient
from data.config import Config
from utils.logger import logger


@allure.feature("Management Social Network Images")
@allure.title("Check updating social network image without permission")
@pytest.mark.api
def test_update_social_network_image_forbidden(access_token):
    """Test for forbidden update of social network image"""
    token = access_token

    body = {
        "id": 1,
        "socialNetworkImageRequestDTO": {
            "imagePath": "https://cdn-icons-png.flaticon.com/512/733/733547.png",
            "hostPath": "https://www.instagram.com"
        },
        "file": "string"
    }

    with allure.step("Create social network images client"):
        client = SocialNetworkImagesClient(
            base_url=Config.BASE_API_URL,
            access_token=token
        )

    with allure.step("Send PUT request to update social network image"):
        response = client.update_social_network_image(body=body)
        logger.info("Response status code: %s", response.status_code)
        logger.info("Response text: %s", response.text)

    with allure.step("Validate response status code"):
        assert response.status_code == 403, (
            f"Expected status code 403, but got {response.status_code}: "
            f"{response.text}"
        )

    with allure.step("Validate error response body"):
        response_json = response.json()
        logger.info("Response json: %s", response_json)
        assert response_json is not None
        assert isinstance(response_json, dict)
        assert "error" in response_json, "Expected 'error' field in response JSON"
        assert response_json["error"] == "Forbidden"
