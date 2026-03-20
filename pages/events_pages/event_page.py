"""This module contains the EventPage class,which represents the event page of a website.
 It inherits from the BasePage class and provides specific locators and methods
for interacting with the event page elements."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.common_pages.places_page import PlacesPage
from pages.events_pages.create_update_event_page import CreateEventPage
from components.events_components.event_card_component import EventCardComponent
from utils.custom_web_element import CustomWebElement


class EventPage(BasePage):
    """Page object for the event page."""

    locators = {
        "main_header_locator": (By.CSS_SELECTOR, ".top-header>.main-header"),
        "create_event_button": (By.CSS_SELECTOR, "div.create button.m-btn"),
        "event_card": (By.CSS_SELECTOR, "mat-card.event-list-item")
    }

    _event_card_pattern = ("//mat-card[contains(@class, 'event-list-item')]"
                           "[.//p[contains(@class, 'event-name') and normalize-space()='{}']]")

    main_header_locator: CustomWebElement
    create_event_button: CustomWebElement
    event_card: CustomWebElement

    @allure.step("Navigating to the Places page")
    def go_to_places(self) -> "PlacesPage":
        """Navigate to the Places page."""
        self.header.click_places_link()
        self.get_wait().until(
            EC.url_contains("places")
        )
        return PlacesPage(self.driver)

    @allure.step("Click Create Event button")
    def click_create_event(self) -> "CreateEventPage":
        """Click 'Create event' button."""
        self.create_event_button.click()

        self.get_wait().until(EC.url_contains("create"))

        return CreateEventPage(self.driver)

    def get_event_card_by_name(self, name) -> EventCardComponent:
        """Finds an event card element by the event's name."""
        formatted_pattern = self._event_card_pattern.format(name)
        event_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        return EventCardComponent(event_card_element)

    def is_loaded(self):
        """Checks that Event Page is loaded by event card presence."""
        event_card_locator = self.locators["event_card"][:2]
        return self._is_loaded_indicator(event_card_locator)
