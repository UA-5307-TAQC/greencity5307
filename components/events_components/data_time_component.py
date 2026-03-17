"""
Component representing date and time picker block.
"""
import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class DateTimeComponent(BaseComponent):
    """Component for date + time + all day checkbox."""

    locators = {
        "date_input": (By.CSS_SELECTOR, "input[formcontrolname='day']"),
        "start_time_input": (By.CSS_SELECTOR, "input[formcontrolname='startTime']"),
        "end_time_input": (By.CSS_SELECTOR, "input[formcontrolname='finishTime']"),
        "all_day_checkbox": (By.CSS_SELECTOR, "mat-checkbox input[type='checkbox']")
    }

    date_input: CustomWebElement
    start_time_input: CustomWebElement
    end_time_input: CustomWebElement
    all_day_checkbox: CustomWebElement

    @allure.step("Set date: {date_value}")
    def set_date(self, date_value: str):
        """Set date value."""
        wait = WebDriverWait(self.root.parent, 5)

        field = self.date_input
        field.click()

        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)

        wait.until(lambda d: field.get_attribute("value") in ("", None))

        field.send_keys(date_value)
        field.send_keys(Keys.TAB)

    @allure.step("Get date value")
    def get_date(self) -> str:
        """Return date value."""
        return self.date_input.get_attribute("value")

    @allure.step("Set start time: {time_value}")
    def set_start_time(self, time_value: str):
        """Set start time."""
        wait = WebDriverWait(self.root.parent, 5)

        field = self.start_time_input

        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)

        wait.until(lambda d: field.get_attribute("value") in ("", None))

        field.send_keys(time_value)
        field.send_keys(Keys.TAB)

    @allure.step("Set end time: {time_value}")
    def set_end_time(self, time_value: str):
        """Set end time."""
        wait = WebDriverWait(self.root.parent, 5)

        field = self.end_time_input

        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)

        wait.until(lambda d: field.get_attribute("value") in ("", None))

        field.send_keys(time_value)
        field.send_keys(Keys.TAB)

    @allure.step("Get start time value")
    def get_start_time(self) -> str:
        """Return start time."""
        return self.start_time_input.get_attribute("value")

    @allure.step("Get end time value")
    def get_end_time(self) -> str:
        """Return end time."""
        return self.end_time_input.get_attribute("value")

    @allure.step("Set All Day checkbox: {value}")
    def set_all_day(self, value: bool):
        """Check or uncheck All Day checkbox."""
        checkbox = self.all_day_checkbox

        if checkbox.is_selected() != value:
            checkbox.click()

    @allure.step("Check if All Day is selected")
    def is_all_day(self) -> bool:
        """Return True if All Day is selected."""
        return self.all_day_checkbox.is_selected()

    @allure.step("Set datetime: date={date_value}, start={start_time}, "
                 "end={end_time}, all_day={all_day}")
    def set_datetime(
            self,
            date_value: str,
            start_time: str | None = None,
            end_time: str | None = None,
            all_day: bool = False
    ):
        """Fill full datetime block."""
        self.set_date(date_value)
        self.set_all_day(all_day)

        if not all_day:
            if start_time:
                self.set_start_time(start_time)

            if end_time:
                self.set_end_time(end_time)
