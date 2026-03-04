"""This module contains the OneEventPage class."""
from typing import List

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.events_pages.event_page import EventPage

from components.events_components.event_info_component import EventInfoComponent
from components.common_components.social_media_links_component import SocialMediaLinksComponent

from utils.custom_web_element import CustomWebElement


class OneEventPage(BasePage):
    """Page object for the One Event page."""

    locators = {
        "back_to_events_button": (By.CSS_SELECTOR, ".button-text"),
        "event_title": (By.CSS_SELECTOR, ".event-title"),
        "event_description_locator": (By.CSS_SELECTOR, ".main-right"),

        "event_tags": (By.CSS_SELECTOR, ".event-tags .event-tag", List[CustomWebElement]),

        "info_block_component": (By.CSS_SELECTOR, ".event-info-block", EventInfoComponent),
        "social_media_component": (By.CSS_SELECTOR, ".share-buttons", SocialMediaLinksComponent),

        "save_event_button": (By.CSS_SELECTOR,
                              "div.save-join-event-block button.secondary-global-button"),
        "join_event_button": (By.CSS_SELECTOR,
                              "div.save-join-event-block button.primary-global-button")
    }

    def back_to_events(self):
        """Click the button to return to the Events page"""
        self.back_to_events_button.wait_and_click()
        return EventPage(self.driver)

    def event_info_block(self):
        """Get the event info block component."""
        return self.info_block_component

    def social_media_links(self):
        """Get the social media links component."""
        return self.social_media_component

    def save_event(self):
        """Click the button to save the event if it's not already saved."""
        if "Unsave" not in self.save_event_button.text:
            self.save_event_button.wait_and_click()

    def unsave_event(self):
        """Click the button to unsave the event if it's currently saved."""
        if "Unsave" in self.save_event_button.text:
            self.save_event_button.wait_and_click()

    def join_event(self):
        """Click the button to join the event if it's not already joined."""
        if "Cancel" not in self.join_event_button.text:
            self.join_event_button.wait_and_click()

    def cancel_request(self):
        """Click the button to cancel the join request if it's currently joined."""
        if "Cancel" in self.join_event_button.text:
            self.join_event_button.wait_and_click()

    @property
    def title(self):
        """Get the title of the event."""
        return self.event_title.text

    @property
    def description(self):
        """Get the description of the event."""
        return self.event_description.text

    @property
    def tags(self):
        """Get the list of tags associated with the event."""
        return [tag.text for tag in self.event_tags]
