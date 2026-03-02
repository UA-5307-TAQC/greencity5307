"""Add place modal component."""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class AddPlaceModalComponent(BaseComponent):
    """Add place modal component class."""
    locators = {
        "cancel_button": (By.CSS_SELECTOR,
                          ".btn-wrapper > .secondary-global-button"),
        "add_button": (By.CSS_SELECTOR,
                       ".btn-wrapper > .primary-global-button")
    }

    def close(self):
        """Close modal component."""
        self.cancel_button.click()

    def submit(self):
        """Submit modal form."""
        self.add_button.click()
