"""This module contains the MainPage class, which represents the main page of the application.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the main page elements."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.types import Locators


class MainPage(BasePage):
    """Page object for the main page."""
    there_are_locator: Locators = (By.CSS_SELECTOR, "#stats > h2")

    @property
    def there_are(self) -> WebElement:
        """Function to find there_are_locator on the main page."""
        return self.driver.find_element(*self.there_are_locator)
