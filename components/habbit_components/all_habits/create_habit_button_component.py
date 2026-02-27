"""This module contains the CreateHabitButtonComponent class."""

import allure

from components.base_component import BaseComponent


class CreateHabitButtonComponent(BaseComponent):
    """Component class for the Create Habit button."""

    @allure.step("Clicking Create Habit button on the All Habits page")
    def click_create_habit_btn(self):
        """Click on the Create Habit button."""
        from pages.habit_pages.create_habit_page import CreateHabitPage # pylint: disable=import-outside-toplevel
        self.root.click()
        return CreateHabitPage(self.root.parent)

    def get_button_text(self) -> str:
        """Get the text of the button (e.g., 'Create habit')."""
        return self.root.text

    def is_enabled(self) -> bool:
        """Check if the button is enabled."""
        return self.root.is_enabled()
