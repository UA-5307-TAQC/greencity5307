"""This module contains the HabitProgressFormComponent class,
 which represents the progress form of the Create Habit page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from components.base_component import BaseComponent
from components.calendar_component import CalendarComponent
from utils.types import Locators


class HabitProgressFormComponent(BaseComponent):
    """Component class for the habit progress form of the Create Habit page."""
    progress_bar_locator: Locators = (By.CSS_SELECTOR, "div.days-duration")
    slider_locator: Locators = (By.XPATH, ".//input[@type='range']")
    invite_friends_btn_locator: Locators = (By.CSS_SELECTOR, "div.icon-plus-grey")

    edit_to_do_btn_locator: Locators = (By.CSS_SELECTOR, "a.edit-icon")
    to_do_field_locator: Locators = (By.CSS_SELECTOR, "input.add-field")
    add_to_do_btn_locator: Locators = (By.CSS_SELECTOR, "button.add-btn")
    save_to_do_btn_locator: Locators = (By.XPATH, ".//button[text() [contains(.,'Save')]]")


    def __init__(self, root: WebElement):
        super().__init__(root)
        self.slider = self.root.find_element(*self.slider_locator)
        self.invite_friends_btn = self.root.find_element(*self.invite_friends_btn_locator)
        self.calendar: CalendarComponent = CalendarComponent(self.root)

        self.edit_to_do_btn = self.root.find_element(*self.edit_to_do_btn_locator)


    @allure.step("Get habit progress on Habit form")
    def get_progress(self) -> str:
        """Get habit progress."""
        progress_bar = self.root.find_element(*self.progress_bar_locator)
        try:
            progress = progress_bar.find_element(By.CLASS_NAME, "thumb-label-mobile")
            return progress.text
        except NoSuchElementException:
            return "0%"


    @allure.step("Choose duration for habit on Habit form")
    def choose_duration(self, num_of_days: int):
        """Choose duration for habit."""
        if num_of_days > 56 or num_of_days < 7:
            raise ValueError(f"Invalid number of days: {num_of_days}.")
        for _ in range(num_of_days - 7):
            self.slider.send_keys(Keys.ARROW_RIGHT)


    @allure.step("Click add friends button on Habit form")
    def click_invite_friends_btn(self):
        """Click add friends button on habit form."""
        self.invite_friends_btn.click()


    @allure.step("Add and save to do item on Habit form")
    def add_to_do_item(self, text: str):
        """Add and save to do item on habit form."""
        self.edit_to_do_btn.click()
        self.root.find_element(*self.to_do_field_locator).send_keys(text)
        self.root.find_element(*self.add_to_do_btn_locator).click()
        self.root.find_element(*self.save_to_do_btn_locator).click()
