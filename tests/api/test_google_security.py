"""Test for validation GET request of Google security"""
from json import JSONDecodeError

import allure
import pytest
from jsonschema.validators import validate

from clients.google_security_client import GoogleSecurityClient
from data.config import Config
from schemas.google_security_schema import google_security_schema
from utils.logger import logger


@pytest.mark.parametrize(
    "project_name, lang",
    [("GREENCITY" , "en"),
     ("GREENCITY", "uk")
     ]
)
def test_google_security(project_name: str, lang: str, access_token):
    """Test for validation of Google security authentication."""

    client = GoogleSecurityClient(base_url=Config.BASE_USER_API_URL, access_token=access_token)

    response = client.get_google_security(project_name, lang)

    if response.status_code == 200:
        with allure.step("Validate proper response json format"):
            parsed_data = response.json()
            logger.info(parsed_data)
            try:
                validate(instance=parsed_data, schema=google_security_schema)
                logger.info("✅ JSON validation passed")
            except JSONDecodeError as e:
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
        assert parsed_data["message"] == "Unforbidden access"
    elif response.status_code == 500:
        parsed_data = response.json()
        logger.info(parsed_data)
        assert parsed_data.get("error") == "Internal Server Error"
    else:
        assert False, "Other error"
