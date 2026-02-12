"""Component for the 'Linked social networks' block."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent


class SocialNetworksComponent(BaseComponent):
    """Component for the 'Linked social networks' block."""

    root_locator = (By.CSS_SELECTOR, "app-social-networks")
    add_button_locator = (By.CSS_SELECTOR, "button.add-button.social-btn")

    def __init__(self, parent: WebElement):
        super().__init__(parent)
        self.root: WebElement = parent.find_element(*self.root_locator)

    def get_add_button_text(self) -> str:
        """Return the text of 'Add social network' button."""
        return self.root.find_element(*self.add_button_locator).text

    def click_add_button(self) -> None:
        """Click the 'Add social network' button."""
        self.root.find_element(*self.add_button_locator).click()
