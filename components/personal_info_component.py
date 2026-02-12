"""
Component for Personal info section of profile edit page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class PersonalInfoComponent(BaseComponent):
    """Component representing Personal info block."""

    name_input: Locators = (By.CSS_SELECTOR, "input[formcontrolname='name']")
    city_input: Locators = (By.CSS_SELECTOR, "app-input-google-autocomplete input")
    credo_textarea: Locators = (By.CSS_SELECTOR, "textarea[formcontrolname='credo']")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.name = self.root.find_element(*self.name_input)
        self.city = self.root.find_element(*self.city_input)
        self.credo = self.root.find_element(*self.credo_textarea)

    def fill_name(self, text: str):
        """Fill the personal info field."""
        self.name.clear()
        self.name.send_keys(text)

    def fill_city(self, city: str):
        """Fill the city field."""
        self.city.clear()
        self.city.send_keys(city)

    def fill_credo(self, text: str):
        """Fill the credo field."""
        self.credo.clear()
        self.credo.send_keys(text)
