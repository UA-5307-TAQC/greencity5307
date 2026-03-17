"""Component for Place / Online checkboxes."""

import allure
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class LocationComponent(BaseComponent):
    """Component for Place / Online checkboxes."""

    locators = {
        "checkbox_place": (By.XPATH, ".//label[contains(text(),'Місце')]/ancestor::mat-checkbox"),
        "checkbox_online": (By.XPATH, ".//label[contains(text(),'Онлайн')]/ancestor::mat-checkbox"),
    }

    checkbox_place: CustomWebElement
    checkbox_online: CustomWebElement

    @allure.step("Set Place checkbox: {value}")
    def set_place(self, value: bool = True):
        """Set the 'Place' checkbox."""
        checkbox = self.checkbox_place
        checkbox_input = checkbox.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

        if checkbox_input.is_selected() != value:
            checkbox.click()

    @allure.step("Set Online checkbox: {value}")
    def set_online(self, value: bool = True):
        """Set the 'Online' checkbox."""
        checkbox = self.checkbox_online
        checkbox_input = checkbox.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

        if checkbox_input.is_selected() != value:
            checkbox.click()

    @allure.step("Check if Place checkbox is selected")
    def is_place(self) -> bool:
        """Return True if Place checkbox is selected."""
        return "checked" in self.checkbox_place.get_attribute("class")

    @allure.step("Check if Online checkbox is selected")
    def is_online(self) -> bool:
        """Return True if Online checkbox is selected."""
        return "checked" in self.checkbox_online.get_attribute("class")
