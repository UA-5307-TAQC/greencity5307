"""Component representing event header section (Title + Duration)."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class EventHeaderComponent(BaseComponent):
    """Component for event title and duration section."""

    locators = {
        "title": (By.CSS_SELECTOR, "input[formcontrolname='title']"),
        "duration_select": (By.CSS_SELECTOR, "mat-select[formcontrolname='duration']"),
        "duration_options": (By.CSS_SELECTOR, "mat-option")
    }

    title: CustomWebElement
    duration_select: CustomWebElement
    duration_options: CustomWebElement

    @allure.step("Set event title: {text}")
    def set_title(self, text: str):
        """Set event title."""
        self.title.clear()
        self.title.send_keys(text)

    @allure.step("Get event title")
    def get_title(self) -> str:
        """Get event title."""
        return self.title.get_attribute("value")

    @allure.step("Open duration dropdown")
    def open_duration_dropdown(self):
        """Open duration dropdown."""
        self.duration_select.click()

    @allure.step("Select duration: {value}")
    def select_duration(self, value: str):
        """Select duration."""
        wait = WebDriverWait(self.root.parent, 5)

        self.open_duration_dropdown()

        option = wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//mat-option//span[normalize-space()='{value}']"))
        )

        option.click()

    @allure.step("Get selected duration")
    def get_selected_duration(self) -> str:
        """Get selected duration."""
        return self.duration_select.text.strip()
