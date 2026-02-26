"""This module contains the ToDoListComponent class,
which represents the to-do list of the My Space page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.base_component import BaseComponent


class ToDoListComponent(BaseComponent):
    """Component class for the to-do list of the My Space page."""

    locators = {
        "to_do_items": (By.XPATH, ".//ul[@class='to-do-list to-do-list-min']/li")
    }


    @allure.step("Get list of dictionaries of to-do items from To-do List component")
    def get_to_do_list(self) -> list:
        """Get list of dictionaries of to-do item names, status, and checkbox elements."""

        to_do_items = self.resolve_list("to_do_items")
        to_do_list = []

        for item in to_do_items:
            name = item.find_element(By.XPATH, "./span/span").get_attribute("textContent")

            checkbox_input = item.find_element(By.XPATH, ".//input")
            is_done = checkbox_input.is_selected()

            checkbox_element = item.find_element(By.XPATH, ".//label")

            to_do_list.append(
                {
                    "name": name,
                    "is_done": is_done,
                    "checkbox_input": checkbox_input,
                    "checkbox_element": checkbox_element
                }
            )

        return to_do_list

    @allure.step("Check or uncheck to-do item on To-do List component")
    def click_to_do(self, driver: WebDriver, element: dict):
        """Check or uncheck to-do item and change status."""
        driver.execute_script("arguments[0].wait_and_click();", element["checkbox_element"])
        element["is_done"] = element["checkbox_input"].is_selected()
