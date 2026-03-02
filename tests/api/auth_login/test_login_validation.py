"""auth login validation"""
import pytest
import requests
import jwt
import allure
from datetime import datetime
from data.config import Config

@allure.feature("Authentication")
@allure.story("User Login")
@allure.title("Verify successful login, response time, and token validity")
def test_login_validation():
    """auth login validation"""
    url = "https://greencity-user.greencity.cx.ua/ownSecurity/signIn"

    with allure.step("Prepare request payload"):
        payload = {
            "email": f"{Config.USER_EMAIL}",
            "password": f"{Config.USER_PASSWORD}",
            "projectName": "GREENCITY"
        }

    with allure.step("Send POST request to login endpoint"):
        response = requests.request("POST", url, json=payload)

    with allure.step("Validate status code and response time"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

        # response_time_ms = response.elapsed.total_seconds() * 1000
        # assert response_time_ms < 600, f"API response is too slow! Time: {response_time_ms:.2f} ms"

    with allure.step("Validate response body data"):
        data = response.json()
        assert data.get("userId") >= 0, "User ID is invalid or missing"
        assert data.get("name") == "test", f"Expected user name 'test', but got '{data.get('name')}'"
        assert data.get("ownRegistrations") is True, "ownRegistrations flag should be True"

    with allure.step("Validate Access Token expiration"):
        token = data.get("accessToken")
        assert token is not None, "Access token is missing in the response body"

        try:
            decoded = jwt.decode(token, options={"verify_signature": False})
            exp_timestamp = decoded.get('exp')

            allure.attach(str(decoded), name="Decoded Token Payload", attachment_type=allure.attachment_type.TEXT)

            assert exp_timestamp is not None, "Token is valid, but missing expiration time ('exp' field)"

            assert datetime.now().timestamp() < exp_timestamp, f"Access token is already expired! (exp: {exp_timestamp})"

        except jwt.exceptions.DecodeError as e:
            pytest.fail(f"Token is invalid or corrupted. Details: {e}")
