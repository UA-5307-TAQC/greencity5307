"""
Component for Personal info section of profile edit page.
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class PersonalInfoComponent(BaseComponent):
    """Component representing Personal info block."""

    locators = {
        "name": (By.CSS_SELECTOR, "input[formcontrolname='name']"),
        "city": (By.CSS_SELECTOR, "app-input-google-autocomplete input"),
        "credo": (By.CSS_SELECTOR, "textarea[formcontrolname='credo']")
    }

    name: CustomWebElement
    city: CustomWebElement
    credo: CustomWebElement

    @allure.step("Fill Name field with value: {name}")
    def fill_name(self, name: str):
        """Fill the personal info field."""
        wait = WebDriverWait(self.root.parent, 5)

        field = self.name
        wait.until(lambda d: field.get_attribute("value") != "")
        # time.sleep(0.3)

        field.clear()
        wait.until(lambda d: field.get_attribute("value") == "")
        field.send_keys(name)
        field.send_keys(Keys.TAB)

    @allure.step("Fill City field with value: {city} and select suggestion")
    def fill_city(self, city: str):
        """Fill the city field and select item."""
        wait = WebDriverWait(self.root.parent, 5)
        field = self.city

        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)

        wait.until(lambda d: field.get_attribute("value") in ("", None))

        for char in city:
            field.send_keys(char)

        wait.until(lambda d: field.get_attribute("value") == city)

        suggestion = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-option")))
        suggestion.click()
        field.send_keys(Keys.TAB)

    @allure.step("Fill Credo field with value: {text}")
    def fill_credo(self, text: str):
        """Fill the credo field."""
        wait = WebDriverWait(self.root.parent, 5)

        field = self.credo

        field.clear()
        wait.until(lambda d: field.get_attribute("value") == "")

        field.send_keys(text)
        field.send_keys(Keys.TAB)

    @allure.step("Get Name field value")
    def get_name_value(self) -> str:
        """Get the personal info field."""
        return self.name.get_attribute("value")

    @allure.step("Get City field value")
    def get_city_value(self) -> str:
        """Get the city field."""
        return self.city.get_attribute("value")

    @allure.step("Get Credo field value")
    def get_credo_value(self) -> str:
        """Get the credo field."""
        return self.credo.get_attribute("value")
