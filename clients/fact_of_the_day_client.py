"""Client for interacting with the FactOfTheDayAPI"""

import allure
from clients.base_client import BaseClient

class FactOfTheDayClient(BaseClient):
    """Client for Fact-of-the-Day endpoints"""

    def __init__(self, base_url, access_token=None):
        super().__init__(
            base_url=f"{base_url}",
            access_token=access_token
        )

    @allure.step("Get random fact of the day")
    def get_random_fact(self):
        """Fetch random fact of the day"""
        return self._request(
            method="GET",
            endpoint="/fact-of-the-day/random"
        )
