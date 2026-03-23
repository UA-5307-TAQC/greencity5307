"""
Component representing Material chip set (multi-select chips).
"""
from typing import List
import allure

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class ChipSetComponent(BaseComponent):
    """Component for mat-chip-option group."""

    locators = {
        "chips": (By.CSS_SELECTOR, "mat-chip-option"),
        "chip_label": (By.CSS_SELECTOR, ".mdc-evolution-chip__text-label"),
        "chip_button": (By.CSS_SELECTOR, "button")
    }

    chips: CustomWebElement
    chip_label: CustomWebElement
    chip_button: CustomWebElement

    @allure.step("Get all chip labels")
    def get_all_labels(self) -> List[str]:
        """Return all chip labels."""
        elements = self.root.find_elements(*self.locators["chips"])

        return [
            chip.find_element(*self.locators["chip_label"]).text.strip()
            for chip in elements
        ]

    @allure.step("Select chip with name: {name}")
    def select_chip(self, name: str):
        """Select chip by visible text."""
        elements = self.root.find_elements(*self.locators["chips"])

        for chip in elements:
            label = chip.find_element(*self.locators["chip_label"]).text.strip()

            if label == name:
                chip.click()
                return

        raise ValueError(f"Chip '{name}' not found.")

    @allure.step("Check if chip '{name}' is selected")
    def is_chip_selected(self, name: str) -> bool:
        """Check if chip is selected."""
        elements = self.root.find_elements(*self.locators["chips"])

        for chip in elements:
            label = chip.find_element(*self.locators["chip_label"]).text.strip()

            if label == name:
                button = chip.find_element(*self.locators["chip_button"])
                return button.get_attribute("aria-selected") == "true"

        raise ValueError(f"Chip '{name}' not found.")
