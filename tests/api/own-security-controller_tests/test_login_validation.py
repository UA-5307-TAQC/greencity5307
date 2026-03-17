"""auth login validation"""
import pytest
import jwt
import allure
from datetime import datetime

from jsonschema import validate, ValidationError

from clients.own_security_client import OwnSecurityClient
from data.config import Config
from schemas.own_security.signin_success_schema import signin_success_schema


@allure.feature("Authentication")
@allure.story("User Login")
@allure.title("Verify successful login, response time, and token validity")
def test_login_validation():
    """auth login validation"""

    client = OwnSecurityClient(f"{Config.BASE_USER_API_URL}")
    response = client.sign_in(
        email=Config.USER_EMAIL,
        password=Config.USER_PASSWORD
    )

    with allure.step("Validate status code and response time"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        response_time_ms = response.elapsed.total_seconds() * 1000
        assert response_time_ms < 3000, f"API response is too slow! Time: {response_time_ms:.2f} ms"

    data = response.json()
    with allure.step("Validate response JSON schema"):
        try:
            validate(instance=data, schema=signin_success_schema)
        except ValidationError as e:
            pytest.fail(f"Response JSON schema validation failed: {e.message}")

    with allure.step("Validate response body data"):
        assert data.get("userId") >= 0, "User ID should be a positive integer"
        assert data.get("name") == Config.USER_NAME, f"Expected {Config.USER_NAME}, but got '{data.get('name')}'"
        assert data.get("ownRegistrations") is True, "ownRegistrations flag should be True"

    with allure.step("Validate Access Token expiration"):
        token = data.get("accessToken")

        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            exp_timestamp = decoded.get('exp')

            allure.attach(str(decoded), name="Decoded Token Payload", attachment_type=allure.attachment_type.TEXT)

            assert exp_timestamp is not None, "Token is valid, but missing expiration time ('exp' field)"
            assert datetime.now().timestamp() < exp_timestamp, f"Access token is already expired! (exp: {exp_timestamp})"
        except Exception as e:
            pytest.fail(f"Token is invalid or corrupted. Details: {e}")
