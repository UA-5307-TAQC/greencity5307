"""This module contains the HabitCardComponent class,
which represents a single habit card on the All Habits page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class HabitCardComponent(BaseComponent):
    """Component class for a single habit card."""

    habit_title_locator: Locators = (By.CSS_SELECTOR, ".habit-title, h4")
    add_habit_btn_locator: Locators = (By.CSS_SELECTOR, "button.btn-primary")
    details_btn_locator: Locators = (By.CSS_SELECTOR, "button.btn-secondary")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.habit_title = self.root.find_element(*self.habit_title_locator)
        self.add_habit_btn = self.root.find_element(*self.add_habit_btn_locator)
        self.details_btn = self.root.find_element(*self.details_btn_locator)

    def get_habit_info(self) -> dict:
        """Get habit title and other info."""
        habit_info = {
            "title": self.habit_title.text,
            "is_added": "Added" in self.add_habit_btn.text
        }
        return habit_info

    def click_add_habit_btn(self):
        """Click 'Add habit' button."""
        self.add_habit_btn.click()

    def click_details_btn(self):
        """Click 'More/Details' button."""
        self.details_btn.click()
