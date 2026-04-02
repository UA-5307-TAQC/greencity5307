import allure
import pytest

from clients.event_client import EventClient

from data.config import Config

from tests.api.conftest import access_token

EVENT_ID = 36


@pytest.fixture
def precondition_if_event_saved(access_token):
    """API precondition to ensure the target event is not in the user's saved list.
    Removes the event from favorites before the test execution."""
    event_client = EventClient(
        base_url=Config.BASE_API_URL,
        access_token=access_token
    )

    with allure.step("Precondition:"
                     "Target event has not to be saved on the user account."):
        response = event_client.remove_event_from_favorites(EVENT_ID)
        status_code = response.status_code
        assert status_code in {200, 400}, \
            f"Failed to prep state. Status: {response.status_code}, Body: {response.text}"
