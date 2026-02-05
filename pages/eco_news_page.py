"""This module contains the EcoNewsPage class, which represents the Eco News page of the website."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from utils.types import Locators


class EcoNewsPage(BasePage):
    """Page object for the Eco News page."""
    main_header_locator: Locators = (By.CSS_SELECTOR, ".cont >.main-header")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header: WebElement = self.driver.find_element(*self.main_header_locator)
