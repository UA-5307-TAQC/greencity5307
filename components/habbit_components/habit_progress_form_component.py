"""This module contains the HabitProgressFormComponent class,
 which represents the progress form of the Create Habit page."""

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from components.abstract_pages_components.my_space_components \
    .abstract_page_components.calendar_component import CalendarComponent
from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class HabitProgressFormComponent(BaseComponent):
    """Component class for the habit progress form of the Create Habit page."""

    locators = {
        "progress_bar": (By.CSS_SELECTOR, "div.days-duration"),
        "slider": (By.XPATH, ".//input[@type='range']"),
        "calendar": (By.CSS_SELECTOR, "div.calendar", CalendarComponent),
        "invite_friends_btn": (By.CSS_SELECTOR, "div.icon-plus-grey"),
        "edit_to_do_btn": (By.CSS_SELECTOR, "a.edit-icon"),
        "to_do_field": (By.CSS_SELECTOR, "input.add-field"),
        "add_to_do_btn": (By.CSS_SELECTOR, "button.add-btn"),
        "save_to_do_btn": (By.XPATH, ".//button[text() [contains(.,'Save')]]"),
    }

    progress_bar: CustomWebElement
    slider: CustomWebElement
    calendar: CalendarComponent
    invite_friends_btn: CustomWebElement
    edit_to_do_btn: CustomWebElement
    to_do_field: CustomWebElement
    add_to_do_btn: CustomWebElement
    save_to_do_btn: CustomWebElement

    @allure.step("Get habit progress on Habit form")
    def get_progress(self) -> str:
        """Get habit progress."""
        self.get_wait().until(EC.visibility_of(self.progress_bar))
        try:
            progress = self.progress_bar.find_element(By.CLASS_NAME,
                                                      "thumb-label-mobile")
            return progress.text
        except NoSuchElementException:
            return "0%"

    @allure.step("Choose duration for habit on Habit form")
    def choose_duration(self, num_of_days: int):
        """Choose duration for habit."""
        if num_of_days > 56 or num_of_days < 7:
            raise ValueError(f"Invalid number of days: {num_of_days}.")
        for _ in range(num_of_days - 7):
            self.get_wait().until(EC.visibility_of(self.slider)).send_keys(
                Keys.ARROW_RIGHT)

    @allure.step("Click add friends button on Habit form")
    def click_invite_friends_btn(self):
        """Click add friends button on habit form."""
        self.invite_friends_btn.wait_and_click()

    @allure.step("Add and save to do item on Habit form")
    def add_to_do_item(self, text: str):
        """Add and save to do item on habit form."""
        self.edit_to_do_btn.wait_and_click()
        self.get_wait().until(EC.visibility_of(self.to_do_field)).send_keys(text)
        self.add_to_do_btn.wait_and_click()
        self.save_to_do_btn.wait_and_click()
