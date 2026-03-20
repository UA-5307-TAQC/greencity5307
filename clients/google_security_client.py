"""Client for validation of request to google security controller"""
from clients.base_client import BaseClient


class GoogleSecurityClient(BaseClient):
    """Class for validation of request to google security controller"""

    def __init__(self, base_url, access_token=None):
        """Init GoogleSecurityClient."""
        super().__init__(base_url=f"{base_url}/googleSecurity", access_token=access_token)

    def get_google_security(self, project_name , lang):
        """Method for getting GET request to Google security"""
        params = {
            "token" : self.access_token,
            "projectName" : project_name,
            "lang": lang,
        }

        return self._request(
            method="GET",
            endpoint="",
            params=params
        )
