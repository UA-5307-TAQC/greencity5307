"""Validation  requests for social networks """

import pytest
import allure

from clients.social_network_client import SocialNetworkClient
from data.config import Config
@pytest.mark.parametrize(
    "image_url , status_code" ,[
        ("https://picsum.photos/200", 403),
        ("https://picsum.photos/200", 403),
        ("https://picsum.photos/200", 403),
        ("https://picsum.photos/200", 403)
    ]
)
@allure.feature("SocialNetwork")
@allure.title("Check user access for image of social network.")
def test_social_networks_get_image(image_url, status_code, access_token):
    """Testing of social networks image get request"""
    token = access_token

    with allure.step("Create social networks client"):
        client = SocialNetworkClient(
            base_url=Config.BASE_USER_API_URL,
            access_token=token
        )
    image_url = "https://picsum.photos/200"

    response = client.get_image_social_networks(url=image_url)

    assert response.status_code == status_code, response.text

@pytest.mark.parametrize(
    "network_id , status_code" ,[
        ("1", 403),
        ("2", 403),
        ("3", 403),
        ("4", 403)
    ]
)
@allure.feature("SocialNetwork")
@allure.title("Check user access to the deletion of social media.")
def test_social_networks_delete_by_id(network_id, status_code ,access_token):
    """Test for deletion of social_network by id verification"""
    token = access_token

    with allure.step("Create social networks client"):
        client = SocialNetworkClient(
            base_url=Config.BASE_USER_API_URL,
            access_token=token
        )

    response = client.delete_social_network_by_id(network_id=network_id)

    assert response.status_code == status_code, response.text
