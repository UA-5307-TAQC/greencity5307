"""This file is for update habit progress page."""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.update_habit_components import HabitBasicInfoComponent, HabitProgressComponent

class UpdateHabitPage(BasePage):
    """Page object for the Update Habit page."""

    locators = {
        "form_root": (By.TAG_NAME, "form", HabitBasicInfoComponent),
        "progress_root": (By.CSS_SELECTOR, ".duration", HabitProgressComponent),
        "save_button": (By.CSS_SELECTOR, "button[type='submit']")
    }

    form_root: HabitBasicInfoComponent
    progress_root: HabitProgressComponent

    def save_changes(self):
        """This function is used to save the changes to the page."""
        self.save_button.click()
