"""File to test mutual friends by API."""

import allure
from jsonschema import validate

from clients.friends_client import FriendsClient
from data.config import Config
from schemas.friends.mutual_friend_schema import mutual_friend_schema

from tests.conftest import dynamic_friend_id


@allure.epic("GreenCity API")
@allure.feature("Friends API")
@allure.story("Get mutual friends")
@allure.title("Verify user can get list of mutual friends via API.")
def test_get_mutual_friends(access_token, dynamic_friend_id):
    """Test to verify get mutual friends."""

    with allure.step("Step 1: Initialize client and send request."):
        client = FriendsClient(base_url=Config.BASE_API_URL, access_token=access_token)

        response = client.get_mutual_friends(friend_id=dynamic_friend_id)

    with allure.step("Step 2: Verify status code is 200 OK."):
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    with allure.step("Step 3: Validate response JSON schema."):
        validate(instance=response.json(), schema=mutual_friend_schema)