"""This module contains the NewsFilterComponent class."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class NewsFilterComponent(BaseComponent):
    """Component for the filter list (tags) on My News page."""

    filter_buttons_locator: Locators = (By.CSS_SELECTOR, ".custom-chip")


    def __init__(self, root: WebElement):
        super().__init__(root)
        self.filter_buttons = self.root.find_elements(*self.filter_buttons_locator)

    def get_filter_by_name(self, name: str) -> WebElement:
        """Finds a specific filter button by its text."""
        for btn in self.filter_buttons:
            if name.lower() in btn.text.lower():
                return btn
        raise ValueError(f"Filter with name '{name}' not found")

    def filter_by(self, name: str):
        """Clicks on a filter with the specified name."""
        btn = self.get_filter_by_name(name)
        btn.click()
