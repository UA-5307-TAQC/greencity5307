"""This module contains the SavedAbstract class,
which represents the saved_abstract page of a website."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators


class SavedAbstract(BasePage):
    """Page object for the saved_abstract page."""

    section_heading= (By.CSS_SELECTOR, "div > .main-header")
    tabs = (By.CSS_SELECTOR, "div>.tabs")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_tab(self, index: int):
        self.find_all(self.tabs)[index].click()

    def get_section_heading(self):
        return self.find(self.section_heading).text
    def is_loaded(self):
        return self.find_all(self.tabs)[0].is_displayed()