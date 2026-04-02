"""Sign up new user test"""
import time
import requests
import allure
from behave import given, when, then
from mailosaur.models import SearchCriteria

@given('a new user with a unique email address')
def create_new_user(context):
    """create new user"""
    server_id = context.api_settings.MAILOSAUR_SERVER_ID
    context.test_email = f"oleg{int(time.time())}@{server_id}.mailosaur.net"
    context.test_name = "Oleg1324"


@when('register the user via the security API')
def register_new_user(context):
    """send api request to register new user"""
    with allure.step("Register new user"):
        response = context.client.sign_up(
            name=context.test_name,
            email=context.test_email,
            password=context.user_password
        )
        assert response.status_code == 201, f"Registration failed: {response.text}"


@then('should receive a verification email via Mailosaur')
def check_mailosaur_email(context):
    """get the link from Mailosaur"""
    with allure.step("Extract verification link from Mailosaur"):
        criteria = SearchCriteria()
        criteria.sent_to = context.test_email

        server_id = context.api_settings.MAILOSAUR_SERVER_ID
        email = context.mailosaur.messages.get(server_id, criteria)

        assert email.html.links, "No links found in verification email"
        context.verification_link = email.html.links[0].href
        assert context.verification_link, "Verification link is empty"


@then('navigate to the verification link')
def send_verification_email(context):
    """send verification email"""
    with allure.step("Verify user via GET request"):
        response = requests.get(context.verification_link, timeout=15)
        assert response.status_code == 200, f"Verification failed with status {response.status_code}"
        time.sleep(10)

@then('should be able to sign in and receive an access token')
def signing(context):
    """sign in and receive an access token"""
    with allure.step("Verify user can sign in"):
        login_response = context.client.sign_in(
            email=context.test_email,
            password=context.user_password
        )

        assert login_response.status_code == 200, f"Login failed: {login_response.text}"

        data = login_response.json()
        assert "accessToken" in data, "Login response missing access token"
        context.auth_token = data["accessToken"]
