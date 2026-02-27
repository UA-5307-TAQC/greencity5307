"""This module contains the SavedAbstract class,
which represents the saved_abstract page of a website."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SavedAbstract(BasePage):
    """Page object for the saved_abstract page."""
    locators ={
         "section_heading": (By.CSS_SELECTOR, "div > .main-header"),
         "tabs": (By.CSS_SELECTOR, "div>.tabs")
    }

    def open_tab(self, index: int):
        """Clicks the tab at the specified index."""
        tabs = self.resolve_list("tabs")

        if index < 0 or index >= len(tabs):
            raise IndexError(f"Tab index must be between 0 and {len(tabs) - 1}")

        tabs[index].wait_and_click()

    def get_section_heading(self) -> str:
        """Gets the text of the section heading."""
        return self.section_heading.text

    def is_loaded(self) -> bool:
        """Checks if the page is loaded."""
        tabs = self.resolve_list("tabs")
        return len(tabs) > 0 and tabs[0].is_displayed()
