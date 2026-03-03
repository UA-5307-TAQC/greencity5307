"""Profile privacy component"""

import time
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent


class ProfilePrivacyComponent(BaseComponent):
    """Component for the 'Profile privacy' block."""

    locators = {
        "root": (By.CSS_SELECTOR, "div.privacy-wrapper"),
        "setting_item": (By.CSS_SELECTOR, "li.ng-star-inserted"),
        "show_location_select": (By.XPATH, ".//li[1]//mat-select"),
        "show_eco_places_select": (By.XPATH, ".//li[2]//mat-select"),
        "show_todo_select": (By.XPATH, ".//li[3]//mat-select"),
        "mat_option": (By.CSS_SELECTOR, "mat-option"),
    }

    root: WebElement
    setting_item: WebElement
    show_location_select: WebElement
    show_eco_places_select: WebElement
    show_todo_select: WebElement
    mat_option: WebElement

    @allure.step("Get 'Show my location' value")
    def get_show_location_value(self) -> str:
        """Get 'Show my location' value."""
        return self.show_location_select.text.strip()

    @allure.step("Get 'Show my eco places' value")
    def get_show_eco_places_value(self) -> str:
        """Get 'Show my eco places' value."""
        return self.show_eco_places_select.text.strip()

    @allure.step("Get 'Show my To-do list' value")
    def get_show_todo_value(self) -> str:
        """Get 'Show my To-do list' value."""
        return self.show_todo_select.text.strip()

    def _set_value(self, select_element: WebElement, value: str):
        """Helper method to set value."""
        wait = WebDriverWait(self.root.parent, 5)

        select_element.click()

        options = wait.until(EC.presence_of_all_elements_located(self.locators["mat_option"]))
        time.sleep(0.2)
        for option in options:
            if option.text.strip() == value:
                option.click()
                time.sleep(0.1)
                break

    @allure.step("Set 'Show my location' to {value}")
    def set_show_location_value(self, value: str):
        """Set 'Show my location' to '{value}'."""
        self._set_value(self.show_location_select, value)

    @allure.step("Set 'Show my eco places' to {value}")
    def set_show_eco_places_value(self, value: str):
        """Set 'Show my eco places' to '{value}'."""
        self._set_value(self.show_eco_places_select, value)

    @allure.step("Set 'Show my To-do list' to {value}")
    def set_show_todo_value(self, value: str):
        """Set 'Show my To-do list' to '{value}'."""
        self._set_value(self.show_todo_select, value)
