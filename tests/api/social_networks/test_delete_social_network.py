"""Social network delete by id verification"""
# pylint: disable=duplicate-code
import allure
import pytest
from jsonschema.exceptions import ValidationError
from jsonschema.validators import validate

from clients.social_network_client import SocialNetworkClient
from data.config import Config
from schemas.social_networks_schema import social_networks_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "network_id, status_code, message, message_type", [
        ("1", 403, "Forbidden", "error"),
        ("32", 403, "Forbidden", "error"),
        ("2", 403, "Forbidden", "error"),
        ("77", 403, "Forbidden", "error"),
        ("90", 403, "Forbidden", "error")
    ]
)
@allure.feature("SocialNetwork")
@allure.title("Check user access to the deletion of social media.")
def test_social_networks_delete_by_id(network_id, status_code, message, message_type, access_token):
    """Test for deletion of social_network by id verification"""
    token = access_token

    with allure.step("Create social networks client"):
        client = SocialNetworkClient(
            base_url=Config.BASE_USER_API_URL,
            access_token=token
        )

    response = client.delete_social_network_by_id(network_id=network_id)

    assert response.status_code == 200, f"Expected status code {status_code}, got {status_code}"
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
        else:
            pytest.fail(f"Response JSON does not match schema: {status_code}")

    assert response.status_code == status_code, \
        f"Expected status code {status_code}, got {response.status_code}"
    parsed_data = response.json()
    logger.info(parsed_data)
    assert parsed_data[message_type] == message, \
        f"Expected message '{message}', got '{parsed_data[message_type]}'"
