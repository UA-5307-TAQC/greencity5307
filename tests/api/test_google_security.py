"""Test for validation GET request of Google security"""
import pytest

from clients.google_security_client import GoogleSecurityClient
from data.config import Config


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

    assert response.status_code == 200, response.text
