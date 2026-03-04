"""This module contains the CreateHabitPage class, which represents the Create Habit page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.habbit_components.habit_basic_info_form_component import HabitBasicInfoFormComponent
from components.habbit_components.habit_progress_form_component import HabitProgressFormComponent
from pages.base_page import BasePage
from utils.custom_web_element import CustomWebElement


class CreateHabitPage(BasePage):
    """Class for the Create Habit page."""

    locators = {
        "page_title": (By.CSS_SELECTOR, ".create-habit-header .header-title"),
        "form_instruction": (By.CSS_SELECTOR, ".create-habit-header p"),
        "basic_form": (By.CSS_SELECTOR, "form.habit-form", HabitBasicInfoFormComponent),
        "progress_form": (By.CSS_SELECTOR, "div.habit-info-block", HabitProgressFormComponent)
    }

    page_title: CustomWebElement
    form_instruction: CustomWebElement
    basic_form: HabitBasicInfoFormComponent
    progress_form: HabitProgressFormComponent

    @allure.step("Get form instruction")
    def get_instruction(self) -> str:
        """Get form instruction."""
        return self.get_wait().until(EC.visibility_of(self.form_instruction)).text

    @allure.step("Get title of Habit page")
    def get_page_header(self) -> str:
        """Get title of Habit page."""
        return self.get_wait().until(EC.visibility_of(self.page_title)).text
