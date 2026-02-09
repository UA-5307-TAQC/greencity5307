"""Component for the 'Linked social networks' block."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

class SocialNetworksComponent:
    """Component for the 'Linked social networks' block."""

    root_locator = (By.CSS_SELECTOR, "app-social-networks")
    add_button_locator = (By.CSS_SELECTOR, "button.add-button.social-btn")

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.root: WebElement = driver.find_element(*self.root_locator)

    def get_add_button_text(self) -> str:
        """Return the text of 'Add social network' button."""
        button = self.root.find_element(*self.add_button_locator)
        return button.text

    def click_add_button(self):
        """Click the 'Add social network' button."""
        button = self.root.find_element(*self.add_button_locator)
        button.click()
