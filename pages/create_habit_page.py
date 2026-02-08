"""This module contains the CreateHabitPage class, which represents the Create Habit page."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from components.habit_basic_info_form_component import HabitBasicInfoFormComponent
from components.habit_progress_form_component import HabitProgressFormComponent
from utils.types import Locators


class CreateHabitPage(BasePage):
    """Class for the Create Habit page."""
    page_title_locator: Locators = (By.CSS_SELECTOR, ".create-habit-header .header-title")
    form_instruction_locator: Locators = (By.CSS_SELECTOR, ".create-habit-header p")
    basic_form_root_locator: Locators = (By.CLASS_NAME, "habit-form")
    progress_form_root_locator: Locators = (By.CLASS_NAME, "habit-info-block")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.page_title: WebElement = self.driver.find_element(*self.page_title_locator)
        self.form_instruction = self.driver.find_element(*self.form_instruction_locator)
        basic_form_root = self.driver.find_element(*self.basic_form_root_locator)
        progress_form_root = self.driver.find_element(*self.progress_form_root_locator)
        self.basic_form: HabitBasicInfoFormComponent = HabitBasicInfoFormComponent(basic_form_root)
        self.progress_form: HabitProgressFormComponent = (
            HabitProgressFormComponent(progress_form_root)
        )


    def get_instruction(self) -> str:
        """Get form instruction."""
        return self.form_instruction.text

    def get_page_header(self) -> str:
        """Get title of Habit page."""
        return self.page_title.text


    def get_basic_form(self) -> HabitBasicInfoFormComponent:
        """Get basic form of Habit page."""
        return self.basic_form


    def get_progress_form(self) -> HabitProgressFormComponent:
        """Get progress form of Habit page."""
        return self.progress_form
