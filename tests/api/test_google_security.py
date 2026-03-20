"""Test for validation GET request of Google security"""

import allure
import pytest
from jsonschema.exceptions import ValidationError
from jsonschema import validate

from clients.google_security_client import GoogleSecurityClient
from data.config import Config
from schemas.google_security_schema import google_security_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "project_name, lang, status_code, message_type,  message",
    [("GREENCITY" , "en", 200, "", ""),
     ("GREENCITY", "uk", 200,"", ""),
     ("", "uk", 404, "message" ,"Page is not found")
     ]
)
# pylint: disable=too-many-positional-arguments
def test_google_security(project_name: str, lang: str,
                         status_code, message_type, message, access_token):
    """Test for validation of Google security authentication."""

    client = GoogleSecurityClient(base_url=Config.BASE_USER_API_URL, access_token=access_token)

    response = client.get_google_security(project_name, lang)

    if response.status_code == status_code:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=google_security_schema)
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
