"""This module contains the NotificationsPage class."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

from utils.custom_web_element import CustomWebElement


class NotificationsPage(BasePage):
    """Page object for the Notifications page."""

    locators = {}

    _main_filter_pattern = ("//div[contains(@class, 'filter-approach-buttons')]"
                            "//button[normalize-space()='{}']")

    _sub_filter_pattern = (
        "//div[contains(@class, 'filter-buttons') and "
        "not(contains(@class, 'filter-approach-buttons'))]//button[normalize-space()='{}']")

    def click_main_filter_by(self, filter_type: str):
        """Click the certain filter button by text."""
        formatted_pattern = self._main_filter_pattern.format(filter_type)
        raw_element = self.driver.find_element(By.XPATH, formatted_pattern)
        CustomWebElement(raw_element).wait_and_click()

    def click_sub_filter_by(self, sub_option: str):
        """Click the certain filter sub option by text."""
        formatted_pattern = self._sub_filter_pattern.format(sub_option)
        raw_element = self.driver.find_element(By.XPATH, formatted_pattern)
        CustomWebElement(raw_element).wait_and_click()
