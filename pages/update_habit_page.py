"""This file is for update habit progress page."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.update_habit_components import HabitBasicInfoComponent, HabitProgressComponent
from pages.base_page import BasePage


class UpdateHabitPage(BasePage):
    """Page object for the update habit progress page."""
    form_root = (By.TAG_NAME, "form")

    progress_root = (By.CSS_SELECTOR, ".duration")

    save_button = (By.CLASS_NAME, "button[type='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

        form_element = self.driver.find_element(*self.form_root)
        self.basic_info = HabitBasicInfoComponent(form_element)

        try:
            progress_element = self.driver.find_element(*self.progress_root)
            self.progress = HabitProgressComponent(progress_element)
        except NoSuchElementException:
            self.progress = None

    def save_changes(self):
        """Click the save button to save changes."""
        self.driver.find_element(*self.save_button).click()
