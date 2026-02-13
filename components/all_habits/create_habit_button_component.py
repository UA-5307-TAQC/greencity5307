"""This module contains the CreateHabitButtonComponent class."""

from selenium.webdriver.remote.webelement import WebElement
from components.base_component import BaseComponent


class CreateHabitButtonComponent(BaseComponent):
    """Component class for the Create Habit button."""

    def click_create_habit_btn(self):
        """Click on the Create Habit button."""
        self.root.click()

    def get_button_text(self) -> str:
        """Get the text of the button (e.g., 'Create habit')."""
        return self.root.text

    def is_enabled(self) -> bool:
        """Check if the button is enabled."""
        return self.root.is_enabled()
