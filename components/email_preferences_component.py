"""Component for the 'Email Notifications' block."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class EmailPreferencesComponent(BaseComponent):
    """Component representing Email Notifications settings."""

    component_root: Locators = (By.CSS_SELECTOR, "div.email-preferences")

    title_locator: Locators = (By.CSS_SELECTOR, "p.title")

    items_locator: Locators = (By.CSS_SELECTOR, "li")

    checkbox_locator: Locators = (By.CSS_SELECTOR, "input[type='checkbox']")

    frequency_select_locator: Locators = (By.CSS_SELECTOR, "mat-select")

    def __init__(self, root: WebElement):
        component_root = root.find_element(*self.component_root)
        super().__init__(component_root)

        self.title: WebElement = self.root.find_element(*self.title_locator)
        self.items: list[WebElement] = self.root.find_elements(*self.items_locator)

    def get_title_text(self) -> str:
        """Return block title text."""
        return self.title.text

    def get_items_count(self) -> int:
        """Return number of email preference items."""
        return len(self.items)

    def toggle_checkbox(self, index: int):
        """Toggle checkbox by item index."""
        checkbox = self.items[index].find_element(*self.checkbox_locator)
        checkbox.click()

    def open_frequency_select(self, index: int):
        """Open frequency dropdown for item."""
        select = self.items[index].find_element(*self.frequency_select_locator)
        select.click()
