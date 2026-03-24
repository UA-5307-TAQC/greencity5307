"""Add place modal component."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class AddPlaceModalComponent(BaseComponent):
    """Add place modal component class."""
    locators = {
        "cancel_button": (By.CSS_SELECTOR,
                          ".btn-wrapper > .secondary-global-button"),
        "add_button": (By.CSS_SELECTOR,
                       ".btn-wrapper > .primary-global-button")
    }

    cancel_button: CustomWebElement
    add_button: CustomWebElement

    def close(self):
        """Close modal component."""
        self.cancel_button.click()

    def submit(self):
        """Submit modal form."""
        self.add_button.click()
