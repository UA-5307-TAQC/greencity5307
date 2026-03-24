import time
import requests
import allure
from clients.own_security_client import OwnSecurityClient
from data.config import Config
from mailosaur import MailosaurClient
from mailosaur.models import SearchCriteria


@allure.title("Test Sign Up - Successful Creation and Email Verification")
def test_signup_and_verify():
    client = OwnSecurityClient(Config.BASE_USER_API_URL)

    server_id = "hgteg6fv"
    test_email = f"oleg{int(time.time())}@{server_id}.mailosaur.net"
    test_name = "Oleg1324"

    with allure.step("1. Register new user"):
        response = client.sign_up(
            name=test_name,
            email=test_email,
            password=Config.USER_PASSWORD
        )

        assert response.status_code == 201, "User registration failed"

    with allure.step("2. Extract verification link from Mailosaur"):
        mailosaur = MailosaurClient(Config.MAILOSAUR_API_KEY)

        criteria = SearchCriteria()
        criteria.sent_to = test_email

        email = mailosaur.messages.get(server_id, criteria)

        verification_link = email.html.links[0].href
        assert verification_link is not None, "Verification link not found in email"

    with allure.step("3. Verify user via GET request"):
        verify_response = requests.get(verification_link)

        assert verify_response.status_code == 200, f"Verification failed with status {verify_response.status_code}"

    # with allure.step("4. Verify user can sign in after confirmation"):
    #     login_response = client.sign_in(
    #         email=test_email,
    #         password=Config.USER_PASSWORD
    #     )
    #
    #     assert login_response.status_code == 200, f"Login failed after verification. Response: {login_response.text}"
    #
    #     auth_token = login_response.json().get("accessToken")
    #     assert auth_token is not None, "Login response does not contain access token"
