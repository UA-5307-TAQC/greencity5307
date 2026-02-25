"""Components for the buttons on the About Us page."""
import allure
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class AboutUsPageHabitButtonComponent(BaseComponent):
    """Component representing the 'Form Habit' buttons."""
    locators = {
        "section_button_form_habit_one": (By.XPATH,
                                          "//*[@id='main-content']/div[1]/div/button"),
        "section_button_form_habit_two": (By.XPATH,
                                          "//*[@id='main-content']/div[2]/div/div/button")
    }
    section_button_form_habit_one: CustomWebElement
    section_button_form_habit_two: CustomWebElement

    @allure.step("Clicking the 'Form habit' one button")
    def click_form_habit_button_one(self):
        """Click the 'Form habit' one button and return an instance of the MyHabitPage."""
        self.section_button_form_habit_one.wait_and_click()

    @allure.step("Clicking the 'Form habit' two button")
    def click_form_habit_button_two(self):
        """Click the 'Form habit' two button and return an instance of the MyHabitPage."""
        self.section_button_form_habit_two.wait_and_click()
