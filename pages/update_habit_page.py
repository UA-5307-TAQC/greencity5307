"""This file is for update habit progress page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException

from pages.base_page import BasePage
from components.update_habit_components import HabitBasicInfoComponent, HabitProgressComponent

class UpdateHabitPage(BasePage):
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
        self.driver.find_element(*self.save_button).click()