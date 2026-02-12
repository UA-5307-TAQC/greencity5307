"""
Component for Quill rich text editor.
"""

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class QuillEditorComponent(BaseComponent):
    """Component representing Quill editor."""

    editor: Locators = (
        By.CSS_SELECTOR,
        ".ql-editor"
    )

    def set_text(self, text: str):
        """Set text into editor."""
        editor = self.root.find_element(*self.editor)
        editor.clear()
        editor.send_keys(text)

    def get_text(self) -> str:
        """Return editor text."""
        editor = self.root.find_element(*self.editor)
        return editor.text.strip()

    def clear(self):
        """Clear editor content."""
        editor = self.root.find_element(*self.editor)
        editor.clear()
