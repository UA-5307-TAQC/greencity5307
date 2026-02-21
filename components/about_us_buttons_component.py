"""Components for the buttons on the About Us page."""
from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent



class AboutUsPageHabitButtonOneComponent(BaseComponent):
    """Component representing the 'Form Habit' buttons."""
    Locators = Tuple[str, str]
    section_button_form_habit_one: Locators = (
        By.CSS_SELECTOR,
        "#main-content > div.about-section.section > div > button"
    )

    @allure.step("Clicking the 'Form habit' one button")
    def click_form_habit_button_one(self):
        """Click the 'Form habit' one button and return an instance of the MyHabitPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.section_button_form_habit_one)
        ).click()

class AboutUsPageHabitButtonTwoComponent(BaseComponent):
    """Component representing the 'Form Habit' buttons."""
    Locators = Tuple[str, str]
    section_button_form_habit_two: Locators = (
        By.XPATH,
        "//*[@id='main-content']/div[2]/div/div/button"
    )

    @allure.step("Clicking the 'Form habit' two button")
    def click_form_habit_button_two(self):
        """Click the 'Form habit' two button and return an instance of the MyHabitPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.section_button_form_habit_two)
        ).click()
