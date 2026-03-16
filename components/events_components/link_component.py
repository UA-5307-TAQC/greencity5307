"""Component for Online link section (appears after selecting Online checkbox)."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class OnlineLinkComponent(BaseComponent):
    """Component for Online link section."""
    locators = {
        "link_input": (By.CSS_SELECTOR, "input[formcontrolname='onlineLink']"),
        "apply_all_days_checkbox": (By.CSS_SELECTOR, "mat-checkbox[formcontrolname='applyAllDays']")
    }

    link_input: CustomWebElement
    apply_all_days_checkbox: CustomWebElement

    @allure.step("Set online event link: {link}")
    def set_link(self, link: str):
        """Enter online event link."""
        wait = WebDriverWait(self.driver, 5)

        input_field = wait.until(
            EC.visibility_of(self.link_input)
        )

        input_field.clear()
        input_field.send_keys(link)

    @allure.step("Get online event link")
    def get_link(self) -> str:
        """Return online event link."""
        return self.link_input.get_attribute("value")

    @allure.step("Set apply to all days checkbox")
    def set_apply_to_all_days(self, value: bool = True):
        """Set apply to all days checkbox."""
        checkbox = self.apply_all_days_checkbox

        is_checked = "checked" in checkbox.get_attribute("class")

        if is_checked != value:
            checkbox.click()

    @allure.step("Check checkbox")
    def is_apply_to_all_days(self) -> bool:
        """Return apply to all days checkbox."""
        return "checked" in self.apply_all_days_checkbox.get_attribute("class")
