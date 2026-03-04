"""Create eco news client."""
import json

import allure
from requests import Response

from clients.base_client import BaseClient

class CreateEcoNewsClient(BaseClient):
    """Client for interacting with the Eco News API,
         extending BaseClient for common functionality."""

    def __init__(self, base_url, access_token=None):
        """Client for interacting with the Eco News API,
        extending BaseClient for common functionality."""
        super().__init__(base_url=f"{base_url}/eco-news", access_token=access_token)

    @allure.step("Create eco new")
    def create_eco_news_by_data(self, # pylint: disable=too-many-arguments, too-many-positional-arguments
        image_file_path, data) -> Response:
        """Find eco news by page with optional filters and sorting."""

        with open(image_file_path, "rb") as img:
            files = {
                "image": ("image.jpg", img, "image/jpeg"),
                "addEcoNewsDtoRequest": (
                    None,
                    json.dumps(data),
                    "application/json"
                )
            }

            return self._request(
                method="POST",
                endpoint="",
                files=files
            )
