"""
Component representing Event Type section.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver

from components.base_component import BaseComponent
from utils.types import Locators


class EventTypeComponent(BaseComponent):
    """Component for Event Type and Invite selects."""

    event_type_select: Locators = (
        By.CSS_SELECTOR,
        "mat-select[formcontrolname='open']"
    )

    invite_select: Locators = (
        By.XPATH,
        "//mat-label[text()='Invite']/ancestor::mat-form-field//mat-select"
    )

    dropdown_options: Locators = (
        By.XPATH,
        "//mat-option//span"
    )

    def __init__(self, root: WebElement, driver: WebDriver):
        super().__init__(root)
        self.driver = driver

    def select_event_type(self, value: str):
        """Select Event Type."""
        select = self.root.find_element(*self.event_type_select)
        select.click()

        options = self.driver.find_elements(*self.dropdown_options)
        for option in options:
            if option.text.strip() == value:
                option.click()
                return

        raise ValueError(f"Option '{value}' not found.")

    def get_event_type(self) -> str:
        """Get Event Type."""
        select = self.root.find_element(*self.event_type_select)
        return select.text.strip()

    def select_invite(self, value: str):
        """Select Invite."""
        select = self.root.find_element(*self.invite_select)
        select.click()

        options = self.driver.find_elements(*self.dropdown_options)
        for option in options:
            if option.text.strip() == value:
                option.click()
                return

        raise ValueError(f"Option '{value}' not found.")

    def get_invite(self) -> str:
        """Get Invite."""
        select = self.root.find_element(*self.invite_select)
        return select.text.strip()
