"""Comments section component."""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class CommentsFormComponent(BaseComponent):
    """Comments section component class."""

    locators = {
        "input": (By.CSS_SELECTOR,
                  ".comment-textarea-wrapper>.comment-textarea"),
        "submit_button": (By.CSS_SELECTOR,
                          ".input-submit > .primary-global-button"),
    }

    input: CustomWebElement
    submit_button: CustomWebElement

    def type_input(self, text: str):
        """Type the input text into the component."""
        self.input.send_keys(text)

    def submit(self):
        """Submit form."""
        self.submit_button.click()
