"""Conftest file with fixtures for FindFriend tests."""
import allure
from pytest import fixture

from tests.api.conftest import access_token

from clients.friends_client import FriendsClient

from data.config import Config

TARGET_USER_ID = 31


@fixture(scope="function")
def target_user_not_added_to_friends(access_token):
    """API Fixture that verifies if friend request was sent to the target user."""
    with allure.step(f"Precondition: A target user exists in the system "
                     f"who is not yet in the user's friend list"):
        client = FriendsClient(
            base_url=Config.BASE_API_URL,
            access_token=access_token
        )
        response = client.cancel_request(friend_id=TARGET_USER_ID)
        status_code = response.status_code
        assert status_code in {200, 404}, \
            f"Failed to prep state. Status: {response.status_code}, Body: {response.text}"
