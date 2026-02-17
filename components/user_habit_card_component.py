"""
user habit card component
"""
import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class UserHabitCardComponent(BaseComponent):
    """Responsible for one difficult habit on the list"""

    title: Locators = (By.CSS_SELECTOR, ".description .second-row")

    checkbox: Locators = (By.CSS_SELECTOR, "div.third-row > button")

    edit_icon: Locators = (By.CSS_SELECTOR, "button.edit")


    def get_title_text(self) -> str:
        """Get the title of the habit card"""
        return self.root.find_element(*self.title).text

    @allure.step("Clicking the checkbox to mark the habit as complete")
    def click_complete_habit(self):
        """Click the checkbox to mark the habit as complete"""
        self.root.find_element(*self.checkbox).click()

    @allure.step("Clicking the edit icon on the habit card")
    def click_edit_habit(self):
        """Click the edit icon on the habit card"""
        self.root.find_element(*self.edit_icon).click()
