"""This module contains the CalendarComponent class,
 which represents the calendar on a web page."""

import allure

from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class CalendarComponent(BaseComponent):
    """Component class for the calendar on a web page."""

    locators = {
        "month_year": (By.CSS_SELECTOR, "button.monthAndYear"),
        "next_btn": (By.CSS_SELECTOR, "img.arrow-next"),
        "prev_btn": (By.CSS_SELECTOR, "img.arrow-previous"),
        "day": (By.CSS_SELECTOR, "button.current-day span")
    }

    month_year: CustomWebElement
    next_btn: CustomWebElement
    prev_btn: CustomWebElement
    day: CustomWebElement


    @allure.step("Get current date on Calendar component")
    def get_current_date(self) -> str:
        """Get current day, month and year."""
        current_month, current_year = self.month_year.text.split()
        current_day = self.day.text
        return f"{current_day} {current_month} {current_year}"

    @allure.step("Click next button on Calendar component")
    def click_next_btn(self, times: int):
        """Click next button on calendar specific amount of times."""
        for _ in range(times):
            self.next_btn.wait_and_click()

    @allure.step("Click previous button on Calendar component")
    def click_prev_btn(self, times: int):
        """Click previous button on calendar specific amount of times."""
        for _ in range(times):
            self.prev_btn.wait_and_click()
