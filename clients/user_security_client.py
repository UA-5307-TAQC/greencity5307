"""API class for own-security-controller"""
from clients.base_client import BaseClient

class UserSecurityClient(BaseClient):
    """Client class for interacting with the Own Security API."""
    def __init__(self,base_url,access_token = None):
        super().__init__(
            base_url=f"{base_url}/ownSecurity",
            access_token=access_token
        )

    def change_password(self,password,confirm_password):
        """Change the password of the user."""
        payload ={
            "password":password,
            "confirmPassword":confirm_password
        }
        return self._request(
            method="PUT",
            endpoint="/changePassword",
            json=payload
        )
