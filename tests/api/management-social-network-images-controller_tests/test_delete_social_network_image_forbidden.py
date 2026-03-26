"""Social network image deletion forbidden verification"""
# pylint: disable=duplicate-code
import allure
import pytest

from clients.social_network_images_client import SocialNetworkImagesClient
from data.config import Config
from utils.logger import logger


@allure.feature("Management Social Network Images")
@allure.title("Check deletion of social network image without permission")
@pytest.mark.api
def test_delete_social_network_image_forbidden(access_token):
    """Test for forbidden deletion of social network image"""
    token = access_token
    image_id = 1

    with allure.step("Create social network images client"):
        client = SocialNetworkImagesClient(
            base_url=Config.BASE_API_URL,
            access_token=token
        )

    with allure.step("Send DELETE request to delete social network image"):
        response = client.delete_social_network_image(image_id=image_id)
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

        assert "error" in response_json, (
            f'Expected "error" key in response body, got: {response_json}'
        )
        assert response_json["error"] == "Forbidden", (
            f'Expected error "Forbidden", got: {response_json["error"]!r}'
        )