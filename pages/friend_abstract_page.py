"""This module contains the MainPage class, which represents the main page of the application.
It inherits from the BasePage class and provides specific locators
and methods for interacting with the main page elements."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage, WebDriver
from utils.types import Locators


class FriendAbstractPage(BasePage):
    """Page object for the Friend Abstract (other user) page."""
    there_are_locator: Locators = (By.CSS_SELECTOR, "#stats > h2")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.there_are: WebElement = self.driver.find_element(*self.there_are_locator)
