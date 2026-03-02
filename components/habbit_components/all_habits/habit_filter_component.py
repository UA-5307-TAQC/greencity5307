"""This module contains the HabitFilterComponent class,
which represents the filter bar (Tags, Difficulty, Types) on the page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from components.base_component import BaseComponent
from utils.types import Locators


class HabitFilterComponent(BaseComponent):
    """Component class for the habits filter bar."""

    tags_dropdown_locator: Locators = (By.CSS_SELECTOR, ".filters-container\
     app-filter-select:nth-child(1)")
    difficulty_dropdown_locator: Locators = (By.CSS_SELECTOR,
                                             ".filters-container app-filter-select:nth-child(2)")
    types_dropdown_locator: Locators = (By.CSS_SELECTOR, ".filters-container\
     app-filter-select:nth-child(3)")
    reset_all_btn_locator: Locators = (By.CLASS_NAME, "reset-btn")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.tags_dropdown = self.root.find_element(*self.tags_dropdown_locator)
        self.difficulty_dropdown = self.root.find_element(*self.difficulty_dropdown_locator)
        self.types_dropdown = self.root.find_element(*self.types_dropdown_locator)
        self.reset_all_btn = self.root.find_element(*self.reset_all_btn_locator)

    def open_tags_filter(self):
        """Click to open Tags dropdown."""
        self.tags_dropdown.click()

    def open_difficulty_filter(self):
        """Click to open Difficulty dropdown."""
        self.difficulty_dropdown.click()

    def open_types_filter(self):
        """Click to open Types dropdown."""
        self.types_dropdown.click()

    def click_reset_all(self):
        """Click 'Reset all' filters button."""
        self.reset_all_btn.click()
