"""Module that contains client for interacting with the Event API,
extending BaseClient for common functionality."""
from clients.base_client import BaseClient


class EventClient(BaseClient):
    """Client class for interacting with the Events API,
    extending BaseClient for common functionality."""
    def __init__(self, base_url, access_token=None):
        """Initializes the client, configuring the base URL."""
        super().__init__(
            base_url=f"{base_url}/events",
            access_token=access_token
        )

    def remove_event_from_favorites(self, event_id: int):
        """Removes the event from favorites by the event's id."""
        return self._request(
            method="DELETE",
            endpoint=f"/{event_id}/favorites"
        )
