"""Base client for API interactions,
providing common functionality for sending requests and handling responses."""
import uuid

import allure
import requests

from utils.logger import logger

_SENSITIVE_HEADERS = frozenset({"authorization", "cookie", "x-api-key"})
_SENSITIVE_BODY_KEYS = frozenset({"password", "confirmpassword", "token"})


def _redact_headers(headers: dict) -> dict:
    """Return a copy of *headers* with sensitive values replaced by '***REDACTED***'."""
    return {
        k: ("***REDACTED***" if k.lower() in _SENSITIVE_HEADERS else v)
        for k, v in headers.items()
    }


def _redact_body(body: dict | None) -> dict | None:
    """Return a sanitised copy of *body* with credential fields masked."""
    if not isinstance(body, dict):
        return body
    return {
        k: ("***" if k.lower() in _SENSITIVE_BODY_KEYS else v)
        for k, v in body.items()
    }


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

        # Build per-request headers without permanently mutating the session.
        # requests.Session.request() merges these with session headers for this
        # call only, so subsequent requests are not affected.
        request_headers = {"X-Request-ID": str(uuid.uuid4())}
        if headers:
            request_headers.update(headers)

        self.logger.info(
            "Sending %s %s | headers=%s | body=%s",
            method,
            url,
            _redact_headers(dict(self.session.headers) | request_headers),
            _redact_body(kwargs.get("json")),
        )
        response = self.session.request(
            method=method,
            url=url,
            headers=request_headers,
            **kwargs
        )
        return response
