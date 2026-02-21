"""Components for the buttons on the About Us page."""
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent

class AboutUsPageHabitButtonComponent(BaseComponent):
    """Component representing the 'Form Habit' buttons."""
    @allure.step("Clicking the 'Form habit' one button")
    def click_form_habit_button_one(self):
        """Click the 'Form habit' one button and return an instance of the MyHabitPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.root)
        ).click()

    @allure.step("Clicking the 'Form habit' two button")
    def click_form_habit_button_two(self):
        """Click the 'Form habit' two button and return an instance of the MyHabitPage."""
        WebDriverWait(self.root.parent, 10).until(
            EC.element_to_be_clickable(self.root)
        ).click()
