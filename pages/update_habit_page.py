"""This file is for update habit progress page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.update_habit_components import HabitBasicInfoComponent, HabitProgressComponent

from utils.types import Locators

class UpdateHabitPage(BasePage):
    """Page object for the Update Habit page."""

    form_root_locator: Locators = (By.TAG_NAME, "form")

    progress_root_locator: Locators = (By.CSS_SELECTOR, ".duration")

    save_button_locator: Locators = (By.CSS_SELECTOR, "button[type='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        form_element = self.driver.find_element(*self.form_root_locator)
        self.basic_info = HabitBasicInfoComponent(form_element)

        try:
            progress_element = self.driver.find_element(*self.progress_root_locator)
            self.progress = HabitProgressComponent(progress_element)
        except NoSuchElementException:
            self.progress = None

    def save_changes(self):
        """This function is used to save the changes to the page."""
        self.driver.find_element(*self.save_button_locator).click()
