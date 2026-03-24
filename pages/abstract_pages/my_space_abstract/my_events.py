"""Page object for the My Events page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.events_pages.create_update_event_page import CreateEventPage
from utils.custom_web_element import CustomWebElement


class MyEventsPage(BasePage):
    """Page object for the My Events page."""

    locators = {
        "add_event_button": (By.ID, "create-button-event"),
        "favorites_toggle": (By.CSS_SELECTOR,
                             ".buttons-wrapper>.favourites"),
        "online_checkbox": (By.ID, "mat-mdc-checkbox-23-input"),
        "offline_checkbox": (By.ID, "mat-mdc-checkbox-24-input"),
    }

    add_event_button: CustomWebElement
    favorites_toggle: CustomWebElement
    online_checkbox: CustomWebElement
    offline_checkbox: CustomWebElement

    def navigate_to_add_event_page(self) -> CreateEventPage:
        """Navigate to the add event page."""
        self.add_event_button.click()
        return CreateEventPage(self.driver)

    def toggle_favorites(self):
        """Toggle the favorite checkbox."""
        self.favorites_toggle.click()

    def toggle_online_checkbox(self):
        """Toggle the online checkbox."""
        self.online_checkbox.click()

    def toggle_offline_checkbox(self):
        """Toggle the offline checkbox."""
        self.offline_checkbox.click()
