"""
Component for Personal info section of profile edit page.
"""

import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent

class PersonalInfoComponent(BaseComponent):
    """Component representing Personal info block."""

    # name_input: Locators = (By.CSS_SELECTOR, "input[formcontrolname='name']")
    # city_input: Locators = (By.CSS_SELECTOR, "app-input-google-autocomplete input")
    # credo_textarea: Locators = (By.CSS_SELECTOR, "textarea[formcontrolname='credo']")
    #
    # def __init__(self, root: WebElement):
    #     super().__init__(root)
    #     self.name = self.root.find_element(*self.name_input)
    #     self.city = self.root.find_element(*self.city_input)
    #     self.credo = self.root.find_element(*self.credo_textarea)

    locators = {
        "name": (By.CSS_SELECTOR, "input[formcontrolname='name']"),
        "city": (By.CSS_SELECTOR, "app-input-google-autocomplete input"),
        "credo": (By.CSS_SELECTOR, "textarea[formcontrolname='credo']")
    }

    name: WebElement
    city: WebElement
    credo: WebElement


    @allure.step("Fill Name field with value: {text}")
    def fill_name(self, text: str):
        """Fill the personal info field."""
        field = self.name
        time.sleep(0.1)

        field.clear()
        field.send_keys(text)
        field.send_keys(Keys.TAB)

    @allure.step("Fill City field with value: {city} and select suggestion")
    def fill_city(self, city: str):
        """Fill the city field and select item."""
        wait = WebDriverWait(self.root.parent, 5)

        self.city.click()
        self.city.clear()
        time.sleep(0.1)
        self.city.send_keys(city)

        suggestion = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "mat-option")))
        suggestion.click()
        self.city.send_keys(Keys.TAB)

    @allure.step("Fill Credo field with value: {text}")
    def fill_credo(self, text: str):
        """Fill the credo field."""
        field = self.credo
        time.sleep(0.1)

        field.clear()
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
