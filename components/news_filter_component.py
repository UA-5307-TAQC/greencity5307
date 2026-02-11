"""
Component for Tag filter block (News, Events, Education, etc.).
"""
from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class NewsFilterComponent(BaseComponent):
    """Component representing filter by tags block."""

    filter_container: Locators = (By.CSS_SELECTOR, "div[aria-label='filter by items']")

    tag_buttons: Locators = (By.CSS_SELECTOR, "button.tag-button")

    tag_text: Locators = (By.CSS_SELECTOR, "span.text")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.container = self.root.find_element(*self.filter_container)
        self.buttons = self.container.find_elements(*self.tag_buttons)

    def click_filter(self, name: str):
        """Click filter button by visible text."""
        for button in self.buttons:
            text = button.find_element(*self.tag_text).text.strip()
            if text == name:
                button.click()
                return

        raise ValueError(f"Filter '{name}' not found.")

    def get_all_filters(self) -> List[str]:
        """Return list of all available filter names."""
        return [
            button.find_element(*self.tag_text).text.strip()
            for button in self.buttons
        ]
