"""This module contains the EventPage class,which represents the event page of a website.
 It inherits from the BasePage class and provides specific locators and methods
for interacting with the event page elements."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators


class EventPage(BasePage):
    """Page object for the event page."""

    main_header_locator: Locators = (By.CSS_SELECTOR, ".top-header>.main-header")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)
