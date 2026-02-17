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
    eco_news_locator: Locators = (By.CSS_SELECTOR, "li:nth-child(1) > a")
    change_language_block: Locators = (By.CSS_SELECTOR, ' ul > li:nth-child(1) > span')
    language_option_locator: Locators = (By.CSS_SELECTOR, 'ul> li:nth-child(2) > span')

    @property
    def there_are(self) -> WebElement:
        """Function to find there_are_locator on the main page."""
        return self.driver.find_element(*self.there_are_locator)

    @property
    def eco_news(self) -> WebElement:
        """Function to find eco_news_locator on the main page."""
        return self.driver.find_element(*self.eco_news_locator)

    @property
    def change_language_button(self) -> WebElement:
        """Function to find change_language_button on the main page."""
        return self.driver.find_element(*self.change_language_block)

    @property
    def language_option_en(self) -> WebElement:
        """Function to find language_option_locator on the main page."""
        return self.driver.find_element(*self.language_option_locator)
