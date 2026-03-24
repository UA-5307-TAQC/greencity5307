"""This module contains the SavedAbstract class,
which represents the saved_abstract page of a website."""
from selenium.webdriver.common.by import By

from components.abstract_pages_components.saved_tabs_component import SavedTabsComponent
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class SavedAbstract(BasePage):
    """Page object for the saved_abstract page."""
    locators ={
         "section_heading": (By.CSS_SELECTOR, "div > .main-header"),
         "tabs_container": (By.CSS_SELECTOR, "app-saved-section")
    }
    section_heading : CustomWebElement

    def get_tabs_component(self) -> SavedTabsComponent:
        """Return an instance of the SavedTabsComponent."""
        tabs_root = self.driver.find_element(*SavedAbstract.locators["tabs_container"])
        return SavedTabsComponent(tabs_root)

    def go_to_tab(self, tab_name: str):
        """Navigate to a specific tab on the saved abstract page."""
        tabs = self.get_tabs_component()
        tabs.click_tab_by_name(tab_name)
        return self

    def get_section_heading(self) -> str:
        """Gets the text of the section heading."""
        return self.section_heading.text

    def is_loaded(self) -> bool:
        """Checks if the page is loaded."""
        tabs = self.resolve_list("tabs")
        return len(tabs) > 0 and tabs[0].is_displayed()

    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.section_heading.is_displayed()
