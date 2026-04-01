"""
Component representing Event Type section.
"""
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class EventTypeComponent(BaseComponent):
    """Component for Event Type and Invite selects."""

    locators = {
        "event_type_select": (By.CSS_SELECTOR, "mat-select[formcontrolname='open']"),
        "invite_select": (By.CSS_SELECTOR, "mat-select[formcontrolname='invite']"),
        "dropdown_options": (By.XPATH, "//mat-option//span"),
    }

    event_type_select: CustomWebElement
    invite_select: CustomWebElement
    dropdown_options: CustomWebElement

    @allure.step("Select event type: {value}")
    def select_event_type(self, value: str):
        """Select Event Type."""
        wait = WebDriverWait(self.root.parent, 5)

        self.event_type_select.click()

        option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{value}']"))
        )
        option.click()

    @allure.step("Get selected event type")
    def get_event_type(self) -> str:
        """Get Event Type."""
        return self.event_type_select.text.strip()

    @allure.step("Select invite option: {value}")
    def select_invite(self, value: str):
        """Select Invite option."""
        wait = WebDriverWait(self.root.parent, 5)

        self.invite_select.click()

        option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{value}']"))
        )
        option.click()

    @allure.step("Get selected invite option")
    def get_invite(self) -> str:
        """Get Invite option."""
        return self.invite_select.text.strip()
