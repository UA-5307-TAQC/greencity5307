"""Comments section component."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class CommentsFormComponent(BaseComponent):
    """Comments section component class."""
    input_locator: Locators = (By.CSS_SELECTOR,
                               ".comment-textarea-wrapper>.comment-textarea")
    submit_button_locator: Locators = (By.CSS_SELECTOR,
                                       ".input-submit > .primary-global-button")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.input = self.root.find_element(
            *self.input_locator)
        self.submit_button = self.root.find_element(
            *self.submit_button_locator)

    def type_input(self, text: str):
        """Type the input text into the component."""
        self.input.send_keys(text)

    def submit(self):
        """Submit form."""
        self.submit_button.click()
