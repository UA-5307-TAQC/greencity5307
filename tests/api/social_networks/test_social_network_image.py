"""Validation  request for social networks image"""
# pylint: disable=duplicate-code
import pytest
import allure
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from clients.social_network_client import SocialNetworkClient
from data.config import Config
from schemas.social_networks_schema import social_networks_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "image_url " ,[
        "https://picsum.photos/200",
        "https://picsum.photos/200",
        "https://picsum.photos/200",
        "https://picsum.photos/200"
    ]
)
@allure.feature("SocialNetwork")
@allure.title("Check user access for image of social network.")
def test_social_networks_get_image(image_url,  access_token):
    """Testing of social networks image get request"""
    token = access_token

    with allure.step("Create social networks client"):
        client = SocialNetworkClient(
            base_url=Config.BASE_USER_API_URL,
            access_token=token
        )
    response = client.get_image_social_networks(url=image_url)

    if response.status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=social_networks_schema)
                logger.info("JSON validation passed")
            except ValidationError as e:
                allure.attach(str(e), name="Validation Error",
                              attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Response JSON does not match schema: {e}")
    elif response.status_code == 400:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == "Current user has no permission for this action"
    elif response.status_code == 404:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["message"] == "Page is not found"
    elif response.status_code == 403:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data["error"] == "Forbidden"
    elif response.status_code == 500:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data.get("error") == "Internal Server Error"
    else:
        assert False, "Other error"
