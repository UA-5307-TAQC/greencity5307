"""Base client for API interactions,
providing common functionality for sending requests and handling responses."""
import uuid
from typing import Callable

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
        # Optional callback invoked when the server returns 401 so that subclasses
        # or fixtures can supply a token-refresh strategy without subclassing.
        self._token_refresher: Callable[[], str] | None = None

    def set_token_refresher(self, refresher: Callable[[], str]) -> None:
        """Register a zero-argument callable that returns a fresh access token.

        When a request receives an HTTP 401 response, the client will call this
        function once, update the session ``Authorization`` header, and retry
        the original request automatically.

        Example::

            client.set_token_refresher(
                lambda: security_client.refresh_token(rt).json()["accessToken"]
            )
        """
        self._token_refresher = refresher

    @allure.step("Send {method} request to {endpoint}")
    def _request(self, method, endpoint, headers=None, **kwargs):
        """Internal method to send HTTP requests with consistent logging and error handling.

        If the response status is 401 and a ``_token_refresher`` has been
        registered, the token is refreshed and the request is retried once.
        """
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

        if response.status_code == 401 and self._token_refresher is not None:
            self.logger.info(
                "Received 401 for %s %s – attempting token refresh.", method, url
            )
            new_token = self._token_refresher()
            self.access_token = new_token
            self.session.headers.update({"Authorization": f"Bearer {new_token}"})
            self.logger.info("Token refreshed – retrying request.")
            response = self.session.request(
                method=method,
                url=url,
                **kwargs
            )

        return response
