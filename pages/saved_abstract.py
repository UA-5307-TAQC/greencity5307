"""This module contains the SavedAbstract class,
which represents the saved_abstract page of a website."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.types import Locators


class SavedAbstract(BasePage):
    """Page object for the saved_abstract page."""

    section_heading: Locators = (By.CSS_SELECTOR, "div > .main-header")
    tabs: Locators = (By.CSS_SELECTOR, "div>.tabs")

    def open_tab(self, index: int):
        """Clicks the tab at the specified index."""
        self.find_all(self.tabs)[index].click()

    def get_section_heading(self):
        """Gets the text of the section heading."""
        return self.find(self.section_heading).text

    def is_loaded(self):
        """Checks if the page is loaded."""
        return self.find_all(self.tabs)[0].is_displayed()
