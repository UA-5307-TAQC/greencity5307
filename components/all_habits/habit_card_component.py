"""This module contains the HabitCardComponent class,
which represents a single habit card on the All Habits page."""
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class HabitCardComponent(BaseComponent):
    """Component class for a single habit card."""

    habit_title_locator: Locators = (By.CSS_SELECTOR, ".title h2")
    add_habit_btn_locator: Locators = (By.CSS_SELECTOR, "button.primary-global-button")
    details_btn_locator: Locators = (By.CSS_SELECTOR, "button.secondary-global-button")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.habit_title = self.root.find_element(*self.habit_title_locator)
        self.add_habit_btn = self.root.find_element(*self.add_habit_btn_locator)
        self.details_btn = self.root.find_element(*self.details_btn_locator)

    @allure.step("Get habit info")
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

    @allure.step("Clicking on the More button on habit card on All Habits page")
    def click_details_btn(self):
        """Click 'More/Details' button."""
        from pages.one_habit_page import OneHabitPage # pylint: disable=import-outside-toplevel
        self.details_btn.click()
        return OneHabitPage(self.root.parent)
