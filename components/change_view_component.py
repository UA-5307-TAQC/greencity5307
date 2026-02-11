"""Component representing change view buttons (tiles/list)."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class ChangeViewComponent(BaseComponent):
    """Component for switching between tile and list views."""

    table_view_button: Locators = (By.CSS_SELECTOR, "span[aria-label='table view']")
    list_view_button: Locators = (By.CSS_SELECTOR, "span[aria-label='list view']")

    def click_table_view(self):
        """Click on the table view."""
        self.root.find_element(*self.table_view_button).click()

    def click_list_view(self):
        """Click on the list view."""
        self.root.find_element(*self.list_view_button).click()

    def is_table_view_active(self) -> bool:
        """Check if the table view is active."""
        button = self.root.find_element(*self.table_view_button)
        return button.get_attribute("aria-pressed") == "true"

    def is_list_view_active(self) -> bool:
        """Check if the list view is active."""
        button = self.root.find_element(*self.list_view_button)
        return button.get_attribute("aria-pressed") == "true"
