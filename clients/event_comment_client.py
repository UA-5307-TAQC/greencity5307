"""Module that contains client for interacting with the Event Comment API,
extending BaseClient for common functionality."""
import json

from clients.base_client import BaseClient


class EventCommentClient(BaseClient):
    """Client class for interacting with the Events API,
    extending BaseClient for common functionality."""

    def __init__(self, base_url, access_token=None):
        """Initializes the client, configuring the base URL and removing the default
        Content-Type header to correctly support multipart/form-data requests."""
        super().__init__(
            base_url=f"{base_url}/events",
            access_token=access_token
        )
        self.timeout = 10
        if "Content-Type" in self.session.headers:
            del self.session.headers["Content-Type"]

    def create_comment(self, event_id: int, text: str, parent_comment_id: int = 0):
        """Create a new comment under a specific event by id."""
        payload = {
            "text": text,
            "parentCommentId": parent_comment_id
        }

        files = {
            "request": (None, json.dumps(payload))
        }
        return self._request(
            method="POST",
            endpoint=f"/{event_id}/comments",
            files=files,
            timeout=self.timeout
        )

    def delete_comment(self, comment_id: int):
        """Delete a specific comment by id."""
        payload = {
            "commentId": comment_id
        }
        return self._request(
            method="DELETE",
            endpoint=f"/comments/{comment_id}",
            json=payload
        )

    def get_comments_count(self, event_id: int):
        """Fetch the total count of comments for a specific event by id."""
        return self._request(
            method="GET",
            endpoint=f"/{event_id}/comments/count",
            timeout=self.timeout
        )
