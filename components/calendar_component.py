"""This module contains the CalendarComponent class,
 which represents the calendar on a web page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from utils.types import Locators
from components.base_component import BaseComponent


class CalendarComponent(BaseComponent):
    """Component class for the calendar on a web page."""
    month_year_locator: Locators = (By.CSS_SELECTOR, "button.monthAndYear")
    next_btn_locator: Locators = (By.CSS_SELECTOR, "img.arrow-next")
    prev_btn_locator: Locators = (By.CSS_SELECTOR, "img.arrow-previous")
    day_locator: Locators = (
        By.XPATH,
        ".//button[contains(@class,'calendar-grid-day') and contains(@class,'current-day')]/span"
    )


    def __init__(self, root: WebElement):
        super().__init__(root)
        self.month_year = self.root.find_element(*self.month_year_locator)
        self.next_btn = self.root.find_element(*self.next_btn_locator)
        self.prev_btn = self.root.find_element(*self.prev_btn_locator)
        self.day = self.root.find_element(*self.day_locator)


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
            self.next_btn.click()


    @allure.step("Click previous button on Calendar component")
    def click_prev_btn(self, times: int):
        """Click previous button on calendar specific amount of times."""
        for _ in range(times):
            self.prev_btn.click()
