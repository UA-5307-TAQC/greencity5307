"""This module contains the OneEventPage class."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OneEventPage(BasePage):
    """Page object for the One Event page."""
    back_to_events_button_locator = (By.CSS_SELECTOR, ".button-text")

    event_title_locator = (By.CSS_SELECTOR, ".event-title")

    event_description_locator = (By.CSS_SELECTOR, ".main-right")

    event_tags_locator = (By.CSS_SELECTOR, ".event-tags .event-tag")

    event_info_block_locator = (By.CSS_SELECTOR, ".event-info-block")
    event_social_media_links_locator = (By.CSS_SELECTOR, ".share-buttons")

    save_event_button_locator = (By.CSS_SELECTOR,
                                 "div.save-join-event-block button.secondary-global-button")
    join_event_button_locator = (By.CSS_SELECTOR,
                                 "div.save-join-event-block button.primary-global-button")

    def back_to_events(self):
        """Click the button to return to the Events page"""
        from pages.events_pages.event_page import \
            EventPage  # pylint: disable=import-outside-toplevel
        self.driver.find_element(*self.back_to_events_button_locator).click()
        return EventPage(self.driver)

    def event_info_block(self):
        """Get the event info block component."""
        event_info_element = self.driver.find_element(
            *self.event_info_block_locator)
        from components.events_components.event_info_component import \
            EventInfoComponent  # pylint: disable=import-outside-toplevel
        return EventInfoComponent(event_info_element)

    def social_media_links(self):
        """Get the social media links component."""
        social_media_links = self.driver.find_element(
            *self.event_social_media_links_locator)
        from components.common_components.social_media_links_component \
            import \
            SocialMediaLinksComponent  # pylint: disable=import-outside-toplevel
        return SocialMediaLinksComponent(social_media_links)

    def save_event(self):
        """Click the button to save the event if it's not already saved."""
        save_button_element = self.driver.find_element(
            *self.save_event_button_locator)
        if "Unsave" not in save_button_element.text:
            save_button_element.click()

    def unsave_event(self):
        """Click the button to unsave the event if it's currently saved."""
        save_button_element = self.driver.find_element(
            *self.save_event_button_locator)
        if "Unsave" in save_button_element.text:
            save_button_element.click()

    def join_event(self):
        """Click the button to join the event if it's not already joined."""
        join_button_element = self.driver.find_element(
            *self.join_event_button_locator)
        if "Cancel" not in join_button_element.text:
            join_button_element.click()

    def cancel_request(self):
        """Click the button to cancel the join request if it's currently joined."""
        join_button_element = self.driver.find_element(
            *self.join_event_button_locator)
        if "Cancel" in join_button_element.text:
            join_button_element.click()

    @property
    def title(self):
        """Get the title of the event."""
        return self.driver.find_element(*self.event_title_locator).text

    @property
    def description(self):
        """Get the description of the event."""
        return self.driver.find_element(*self.event_description_locator).text

    @property
    def tags(self):
        """Get the list of tags associated with the event."""
        tags_elements = self.driver.find_elements(*self.event_tags_locator)
        return [tag.text for tag in tags_elements]
