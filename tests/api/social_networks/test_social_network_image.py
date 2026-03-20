"""Validation request for social networks image"""
# pylint: disable=duplicate-code
import pytest
import allure
from jsonschema.exceptions import ValidationError
from jsonschema import validate

from clients.social_network_client import SocialNetworkClient
from data.config import Config
from schemas.social_networks_schema import social_networks_image_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "image_url, status_code" ,[
        ("https://picsum.photos/200",200)
    ]
)
@allure.feature("SocialNetwork")
@allure.title("Check user access for image of social network.")
def test_social_networks_get_image_valid(image_url, status_code, access_token):
    """Testing of social networks image get request using valid url"""
    token = access_token

    with allure.step("Create social networks client"):
        client = SocialNetworkClient(
            base_url=Config.BASE_USER_API_URL,
            access_token=token
        )
    response = client.get_image_social_networks(url=image_url)

    if response.status_code == status_code:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=social_networks_image_schema)
                logger.info("JSON validation passed")
            except ValidationError as e:
                allure.attach(str(e), name="Validation Error",
                              attachment_type=allure.attachment_type.TEXT)
                pytest.fail(f"Response JSON does not match schema: {e}")
    else:
        pytest.fail(f"Response JSON does not match schema: {status_code}")

@pytest.mark.parametrize(
    "image_url, status_code, message_type, message" ,[
        ("https://picsum.photos/400",400, "message",
         "Current user has no permission for this action"),
        ("https://picsum.photos/404",404, "message", "Page is not found"),
        ("https://picsum.photos/403",403, "error", "Forbidden"),
        ("https://picsum.photos/500",500, "error", "Internal Server Error")
    ]
)
def test_social_networks_get_image_invalid(image_url, status_code,
                                           message_type, message, access_token):
    """Testing of social networks image get request using invalid url"""
    token = access_token

    with allure.step("Create social networks client"):
        client = SocialNetworkClient(
            base_url=Config.BASE_USER_API_URL,
            access_token=token
        )
    response = client.get_image_social_networks(url=image_url)

    assert response.status_code == status_code,\
        f"Expected status code {status_code}, got {response.status_code}"
    parsed_data = response.json()
    logger.info(parsed_data)
    assert parsed_data[message_type] == message,\
        f"Expected message '{message}', got '{parsed_data[message_type]}'"
