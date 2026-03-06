"""Base client for API interactions,
providing common functionality for sending requests and handling responses."""
import uuid

import allure
import requests

from utils.logger import logger


class BaseClient:
    """Base client for API interactions,
    providing common functionality for sending requests and handling responses."""
    def __init__(self, base_url, access_token=None):
        """Base client for API interactions, handling session management and request logging."""
        self.base_url = base_url
        self.access_token = access_token
        self.session = requests.Session()
        if self.access_token:
            self.session.headers.update({"Authorization": f"Bearer {self.access_token}"})
        self.logger = logger

    @allure.step("Send {method} request to {endpoint}")
    def _request(self, method, endpoint, headers=None, **kwargs):
        """Internal method to send HTTP requests with consistent logging and error handling."""
        url = f"{self.base_url}{endpoint}"

        request_id = str(uuid.uuid4())

        if headers:
            self.session.headers.update(headers)

        self.session.headers["X-Request-ID"] = request_id

        self.logger.info( # pylint: disable=logging-fstring-interpolation
            f"Sending {method} request to {url}"
            f" with headers: {self.session.headers}"
            f" and kwargs: {kwargs}"
        )
        response = self.session.request(
            method=method,
            url=url,
            **kwargs
        )
        return response
