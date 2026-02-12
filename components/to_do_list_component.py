"""This module contains the ToDoListComponent class,
which represents the to-do list of the My Space page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.base_component import BaseComponent
from utils.types import Locators


class ToDoListComponent(BaseComponent):
    """Component class for the to-do list of the My Space page."""
    to_do_items_locator: Locators = (By.XPATH, ".//ul[@class='to-do-list to-do-list-min']/li")

    def get_to_do_list(self) -> list:
        """Get list of dictionaries of to-do item names, status, and checkbox elements."""
        to_do_items = self.root.find_elements(*self.to_do_items_locator)
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


    def click_to_do(self, driver: WebDriver, element: dict):
        """Check or uncheck to-do item and change status."""
        driver.execute_script("arguments[0].click();", element["checkbox_element"])
        element["is_done"] = element["checkbox_input"].is_selected()
