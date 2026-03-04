"""
user habit card component
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent


class UserHabitCardComponent(BaseComponent):
    """Responsible for one difficult habit on the list"""

    locators = {
        "title": (By.CSS_SELECTOR, ".description .second-row"),
        "checkbox": (By.CSS_SELECTOR, "div.third-row > button"),
        "edit_icon": (By.CSS_SELECTOR, "button.edit")
    }

    title: WebElement
    checkbox: WebElement
    edit_icon: WebElement

    def get_title_text(self) -> str:
        """Get the title of the habit card"""
        return self.title.text

    @allure.step("Clicking the checkbox to mark the habit as complete")
    def click_complete_habit(self):
        """Click the checkbox to mark the habit as complete"""
        self.checkbox.click()

    @allure.step("Clicking the edit icon on the habit card")
    def click_edit_habit(self):
        """Click the edit icon on the habit card"""
        self.edit_icon.wait_and_click()
