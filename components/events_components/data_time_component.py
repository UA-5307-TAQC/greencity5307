"""
Component representing date and time picker block.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from components.base_component import BaseComponent
from utils.types import Locators


class DateTimeComponent(BaseComponent):
    """Component for date + time + all day checkbox."""

    date_input: Locators = (
        By.CSS_SELECTOR,
        "input[formcontrolname='day']"
    )

    start_time_input: Locators = (
        By.CSS_SELECTOR,
        "input[formcontrolname='startTime']"
    )

    end_time_input: Locators = (
        By.CSS_SELECTOR,
        "input[formcontrolname='finishTime']"
    )

    all_day_checkbox: Locators = (
        By.CSS_SELECTOR,
        "mat-checkbox input[type='checkbox']"
    )

    def set_date(self, date_value: str):
        """Set date (format: YYYY-MM-DD)."""
        field = self.root.find_element(*self.date_input)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(date_value)
        field.send_keys(Keys.TAB)

    def get_date(self) -> str:
        """Return date value."""
        return self.root.find_element(*self.date_input).get_attribute("value")

    def set_start_time(self, time_value: str):
        """Set start time (format: HH:MM)."""
        field = self.root.find_element(*self.start_time_input)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(time_value)
        field.send_keys(Keys.TAB)

    def set_end_time(self, time_value: str):
        """Set end time (format: HH:MM)."""
        field = self.root.find_element(*self.end_time_input)
        field.send_keys(Keys.CONTROL + "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(time_value)
        field.send_keys(Keys.TAB)

    def get_start_time(self) -> str:
        """Get start time."""
        return self.root.find_element(*self.start_time_input).get_attribute("value")

    def get_end_time(self) -> str:
        """Get end time."""
        return self.root.find_element(*self.end_time_input).get_attribute("value")

    def set_all_day(self, value: bool):
        """Check/uncheck All Day checkbox."""
        checkbox = self.root.find_element(*self.all_day_checkbox)

        is_checked = checkbox.is_selected()

        if value != is_checked:
            checkbox.click()

    def is_all_day(self) -> bool:
        """Return True if All Day is selected."""
        return self.root.find_element(*self.all_day_checkbox).is_selected()

    def set_datetime(
            self,
            date_value: str,
            start_time: str = None,
            end_time: str = None,
            all_day: bool = False
    ):
        """Convenience method to fill full datetime block."""
        self.set_date(date_value)
        self.set_all_day(all_day)

        if not all_day:
            if start_time:
                self.set_start_time(start_time)
            if end_time:
                self.set_end_time(end_time)
