"""This module defines the EventInfoComponent class,
which represents the event information section of an event page."""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from components.base_component import BaseComponent

from utils.custom_web_element import CustomWebElement


class EventInfoComponent(BaseComponent):
    """Component representing the event information section of an event page."""

    locators = {
        "event_duration_item": (By.CSS_SELECTOR, ".event-duration"),
        "event_time_item": (By.CSS_SELECTOR, ".event-date-content div:last-child"),
        "event_location_item": (By.CSS_SELECTOR, ".event-location a"),
        "event_link_item": (By.CSS_SELECTOR, ".event-link a"),
        "event_status_item": (By.CSS_SELECTOR, ".event-status"),
        "event_access_item": (By.CSS_SELECTOR, ".event-status-access-content div:last-child"),
        "event_author_item": (By.CSS_SELECTOR, ".event-author")
    }

    event_duration_item: CustomWebElement
    event_time_item: CustomWebElement
    event_location_item: CustomWebElement
    event_link_item: CustomWebElement
    event_status_item: CustomWebElement
    event_access_item: CustomWebElement
    event_author_item: CustomWebElement

    @property
    def duration(self):
        """Get the duration of the event."""
        return self.event_duration_item.text

    @property
    def time(self):
        """Get the time of the event."""
        return self.event_time_item.text

    @property
    def location_link(self):
        """Get the URL of the event location."""
        return self.event_location_item.get_attribute("href")

    @property
    def event_link(self):
        """Get the URL of the event link, or None if it doesn't exist."""
        try:
            return self.event_link_item.get_attribute("href")
        except NoSuchElementException:
            return None

    @property
    def status(self):
        """Get the status of the event."""
        return self.event_status_item.text

    @property
    def access(self):
        """Get the access level of the event."""
        return self.event_access_item.text

    @property
    def author(self):
        """Get the author of the event."""
        return self.event_author_item.text
