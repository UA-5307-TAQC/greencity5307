"""This module contains the ToDoListComponent class,
which represents the to-do list of the My Space page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class ToDoListComponent(BaseComponent):
    """Component class for the to-do list of the My Space page."""

    locators = {
        "to_do_items": (By.CSS_SELECTOR, "ul.to-do-list li"),
        "item_name": (By.XPATH, "./span/span"),
        "item_input": (By.XPATH, ".//input"),
        "item_label": (By.XPATH, ".//label")
    }

    to_do_items: list
    item_name: CustomWebElement
    item_input: CustomWebElement
    item_label: CustomWebElement


    @allure.step("Get list of dictionaries of to-do items from To-do List component")
    def get_to_do_list(self) -> list:
        """Get list of dictionaries of to-do item names, status, and checkbox elements."""

        to_do_items = self.resolve_list("to_do_items")
        to_do_list = []

        for item in to_do_items:
            name_el = item.find_element(*self.locators["item_name"][:2])
            input_el = item.find_element(*self.locators["item_input"][:2])
            label_el = item.find_element(*self.locators["item_label"][:2])

            to_do_list.append(
                {
                "name": name_el.get_attribute("textContent"),
                "is_done": input_el.is_selected(),
                "checkbox_input": input_el,
                "checkbox_element": label_el
                }
            )

        return to_do_list

    @allure.step("Check or uncheck to-do item on To-do List component")
    def click_to_do(self, driver: WebDriver, element: dict):
        """Check or uncheck to-do item and change status."""
        driver.execute_script("arguments[0].click();", element["checkbox_element"])
        element["is_done"] = element["checkbox_input"].is_selected()
