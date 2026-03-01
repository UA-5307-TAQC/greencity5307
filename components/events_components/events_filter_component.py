"""Component for interacting with the events filter block on the events page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from components.base_component import BaseComponent


class EventsFilterComponent(BaseComponent):
    """Component representing the filter block on the events page."""
    reset_button_locator = (By.CSS_SELECTOR, "button.reset")
    dropdown_trigger_pattern = (".//div[contains(@class, 'dropdown')]"
                                "[.//mat-label[contains(text(), '{}')]]//mat-select")
    option_pattern = "//mat-option//span[contains(text(), '{}')]"

    def _select_filter_value(self, filter_name: str, option_name: str):
        """Helper method to select a value from a dropdown filter."""
        xpath = self.dropdown_trigger_pattern.format(filter_name)
        dropdown = self.root.find_element(By.XPATH, xpath)
        dropdown.click()

        option_xpath = self.option_pattern.format(option_name)
        self.root.parent.find_element(By.XPATH, option_xpath).click()

        dropdown.send_keys(Keys.ESCAPE)

    def filter_by_time(self, time_option: str):
        """Filter events by time using the specified option."""
        self._select_filter_value("Event time", time_option)

    def filter_by_location(self, location_name: str):
        """Filter events by location using the specified location name."""
        self._select_filter_value("Location", location_name)

    def filter_by_status(self, status: str):
        """Filter events by status using the specified status."""
        self._select_filter_value("Status", status)

    def filter_by_type(self, event_type: str):
        """Filter events by type using the specified event type."""
        self._select_filter_value("Type", event_type)

    def click_reset(self):
        """Click the reset button to clear all filters."""
        self.root.find_element(*self.reset_button_locator).click()

    def is_reset_button_enabled(self):
        """Check if the reset button is enabled."""
        btn = self.root.find_element(*self.reset_button_locator)
        return btn.is_enabled()
