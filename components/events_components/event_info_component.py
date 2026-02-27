"""This module defines the EventInfoComponent class,
which represents the event information section of an event page."""
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from components.base_component import BaseComponent


class EventInfoComponent(BaseComponent):
    """Component representing the event information section of an event page."""
    event_duration_locator = (By.CSS_SELECTOR, ".event-duration")
    event_time_locator = (By.CSS_SELECTOR, ".event-date-content div:last-child")
    event_location_locator = (By.CSS_SELECTOR, ".event-location a")
    event_link_locator = (By.CSS_SELECTOR, ".event-link a")
    event_status_locator = (By.CSS_SELECTOR, ".event-status")
    event_access_locator = (By.CSS_SELECTOR, ".event-status-access-content div:last-child")
    event_author_locator = (By.CSS_SELECTOR, ".event-author")

    @property
    def duration(self):
        """Get the duration of the event."""
        return self.root.find_element(*self.event_duration_locator).text

    @property
    def time(self):
        """Get the time of the event."""
        return self.root.find_element(*self.event_time_locator).text

    @property
    def location_link(self):
        """Get the URL of the event location."""
        return self.root.find_element(*self.event_location_locator).get_attribute("href")

    @property
    def event_link(self):
        """Get the URL of the event link, or None if it doesn't exist."""
        try:
            return self.root.find_element(*self.event_link_locator).get_attribute("href")
        except NoSuchElementException:
            return None

    @property
    def status(self):
        """Get the status of the event."""
        return self.root.find_element(*self.event_status_locator).text

    @property
    def access(self):
        """Get the access level of the event."""
        return self.root.find_element(*self.event_access_locator).text

    @property
    def author(self):
        """Get the author of the event."""
        return self.root.find_element(*self.event_author_locator).text
