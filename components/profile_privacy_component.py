"""Profile privacy component"""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class ProfilePrivacyComponent(BaseComponent):
    """Component for the 'Profile privacy' block."""

    locators = {
        "show_location_select": (By.XPATH,
            "//div[contains(text(),'Показувати моє місцезнаходження')]/ancestor::li//mat-select"
        ),
        "show_eco_places_select": (By.XPATH,
            "//div[contains(text(),'Показувати мої еко-місця')]/ancestor::li//mat-select"
        ),
        "show_todo_select": (By.XPATH,
            "//div[contains(text(),'Показувати мій список завдань')]/ancestor::li//mat-select"
        ),
        "mat_option": (By.CSS_SELECTOR, "mat-option"),
    }

    show_location_select: CustomWebElement
    show_eco_places_select: CustomWebElement
    show_todo_select: CustomWebElement
    mat_option: CustomWebElement

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
        wait = WebDriverWait(self.driver, 5)

        select_element.click()

        option_locator = (By.XPATH, f"//mat-option//span[normalize-space()='{value}']")

        option = wait.until(EC.element_to_be_clickable(option_locator))
        option.click()

        wait.until(EC.staleness_of(option))

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
