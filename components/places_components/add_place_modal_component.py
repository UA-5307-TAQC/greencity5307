"""Add place modal component."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class AddPlaceModalComponent(BaseComponent):
    """Add place modal component class."""
    cancel_button_locator: Locators = (By.CSS_SELECTOR,
                                       ".btn-wrapper > .secondary-global-button")
    add_button_locator: Locators = (By.CSS_SELECTOR,
                                    ".btn-wrapper > .primary-global-button")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.cancel_button = self.root.find_element(
            *self.cancel_button_locator)
        self.add_button = self.root.find_element(*self.add_button_locator)

    def close(self):
        """Close modal component."""
        self.cancel_button.click()

    def submit(self):
        """Submit modal form."""
        self.add_button.click()
