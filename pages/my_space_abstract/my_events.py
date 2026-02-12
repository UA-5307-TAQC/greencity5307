"""Page object for the My Events page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.types import Locators


class MyEventsPage(BasePage):
    """Page object for the My Events page."""
    add_event_button_locator: Locators = (By.ID, "create-button-event")
    favorites_toggle_locator: Locators = (By.CSS_SELECTOR,
                                         ".buttons-wrapper>.favourites")
    online_checkbox_locator: Locators = (By.ID, "mat-mdc-checkbox-23-input")
    offline_checkbox_locator: Locators = (By.ID, "mat-mdc-checkbox-24-input")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.add_event_button: WebElement = self.driver.find_element(
            *self.add_event_button_locator)
        self.favorites_toggle: WebElement = self.driver.find_element(
            *self.favorites_toggle_locator)
        self.online_checkbox: WebElement = self.driver.find_element(
            *self.online_checkbox_locator)
        self.offline_checkbox: WebElement = self.driver.find_element(
            *self.offline_checkbox_locator)

    def navigate_to_add_event_page(self):
        """Navigate to the add event page."""
        self.add_event_button.click()

    def toggle_favorites(self):
        """Toggle the favorite checkbox."""
        self.favorites_toggle.click()

    def toggle_online_checkbox(self):
        """Toggle the online checkbox."""
        self.online_checkbox.click()

    def toggle_offline_checkbox(self):
        """Toggle the offline checkbox."""
        self.offline_checkbox.click()
