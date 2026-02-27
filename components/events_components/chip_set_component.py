"""
Component representing Material chip set (multi-select chips).
"""

from typing import List

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class ChipSetComponent(BaseComponent):
    """Component for mat-chip-option group."""

    chips: Locators = (
        By.CSS_SELECTOR,
        "mat-chip-option"
    )

    chip_label: Locators = (
        By.CSS_SELECTOR,
        ".mdc-evolution-chip__text-label"
    )

    def get_all_labels(self) -> List[str]:
        """Return all chip labels."""
        elements = self.root.find_elements(*self.chips)
        return [
            el.find_element(*self.chip_label).text.strip()
            for el in elements
        ]

    def select_chip(self, name: str):
        """Select chip by visible text."""
        elements = self.root.find_elements(*self.chips)

        for chip in elements:
            label = chip.find_element(*self.chip_label).text.strip()
            if label == name:
                chip.click()
                return

        raise ValueError(f"Chip '{name}' not found.")

    def is_chip_selected(self, name: str) -> bool:
        """Check if chip is selected."""
        elements = self.root.find_elements(*self.chips)

        for chip in elements:
            label = chip.find_element(*self.chip_label).text.strip()
            if label == name:
                button = chip.find_element(By.CSS_SELECTOR, "button")
                return button.get_attribute("aria-selected") == "true"

        raise ValueError(f"Chip '{name}' not found.")
