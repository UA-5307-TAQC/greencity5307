"""
Component for Quill rich text editor.
"""

import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement



class QuillEditorComponent(BaseComponent):
    """Component representing Quill editor."""

    locators = {
        "editor": (By.CSS_SELECTOR, ".ql-editor")
    }

    editor: CustomWebElement

    @allure.step("Enter description: {text}")
    def set_description(self, text: str):
        """Set description text."""
        self.editor.clear()
        self.editor.send_keys(text)

    @allure.step("Get description text")
    def get_description(self) -> str:
        """Get description text."""
        return self.editor.text.strip()
