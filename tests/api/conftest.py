import pytest

from clients.friends_client import FriendsClient
from clients.own_security_client import OwnSecurityClient

from data.config import Config


@pytest.fixture(scope="function")
def access_token():
    """Fixture that logs in the user for api tests."""
    client = OwnSecurityClient(Config.BASE_USER_API_URL)
    response = client.sign_in(
        email=Config.USER_EMAIL,
        password=Config.USER_PASSWORD
    )

    assert response.status_code == 200, \
        f"Login failed. Status: {response.status_code}. Response body: {response.text}"

    auth_token = response.json().get("accessToken")
    assert auth_token, \
        f"Login response does not contain access token. Response body: {response.text}"

    return auth_token


@pytest.fixture(scope="function")
def dynamic_friend_id(access_token):
    """Fixture that returns a valid confirmed friend id for current user. """

    client = FriendsClient(base_url=Config.BASE_API_URL, access_token=access_token)
    response = client.get_all_friends()
    assert response.status_code == 200, (f"Failed to fetch friends for fixture, "
                                         f"status code: {response.status_code}")

    data = response.json()
    friends_list = data.get("page", [])

    if not friends_list:
        pytest.skip("Test skipped: No confirmed friends found for current user.")

    return friends_list[0].get("id")
