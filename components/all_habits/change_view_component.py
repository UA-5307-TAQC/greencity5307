"""This module contains the ChangeViewComponent class,
which controls the Grid/List view switcher."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class ChangeViewComponent(BaseComponent):
    """Component class for switching between Grid and List views."""

    grid_btn_locator: Locators = (By.CSS_SELECTOR, "button.btn-tiles")
    list_btn_locator: Locators = (By.CSS_SELECTOR, "button.btn-bars")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.grid_btn = self.root.find_element(*self.grid_btn_locator)
        self.list_btn = self.root.find_element(*self.list_btn_locator)

    def set_grid_view(self):
        """Switch view to Grid (Tiles)."""
        self.grid_btn.click()

    def set_list_view(self):
        """Switch view to List (Bars)."""
        self.list_btn.click()
