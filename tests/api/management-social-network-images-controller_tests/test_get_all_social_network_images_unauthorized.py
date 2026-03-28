"""Social network images get all unauthorized verification"""
# pylint: disable=duplicate-code
import allure
import pytest

from clients.social_network_images_client import SocialNetworkImagesClient
from data.config import Config
from utils.logger import logger


@allure.feature("Management Social Network Images")
@allure.title("Check getting all social network images without authorization")
@pytest.mark.api
def test_get_all_social_network_images_unauthorized():
    """Test for unauthorized getting all social network images"""
    with allure.step("Create social network images client without token"):
        client = SocialNetworkImagesClient(
            base_url=Config.BASE_API_URL
        )

    with allure.step("Send GET request to receive all social network images"):
        response = client.get_all_social_network_images()
        logger.info("Response status code: %s", response.status_code)
        logger.info("Response text: %s", response.text)

    with allure.step("Validate response status code"):
        assert response.status_code == 401, (
            f"Expected status code 401, but got {response.status_code}: "
            f"{response.text}"
        )

    with allure.step("Validate error response body"):
        response_json = response.json()
        logger.info("Response json: %s", response_json)
        assert response_json is not None
        assert isinstance(response_json, dict)

        if "error" in response_json:
            assert response_json["error"] == "Unauthorized"