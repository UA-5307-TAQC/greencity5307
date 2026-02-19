"""
Habit page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.my_space_abstract_page import MySpaceAbstractPage
from utils.types import Locators


class MyHabitPage(MySpaceAbstractPage):
    """ Habit page """
    habit_cards_list: Locators = (By.TAG_NAME, "app-one-habit")
    add_new_habit_button: Locators = (By.XPATH, "//*[@id='create-button-new-habit']/span")

    def is_loaded(self):
        """Method that verifies if My Habit Page is loaded by 'Add New Habit' button."""
        try:
            add_new_habit_button = self.driver.find_element(*self.add_new_habit_button)
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(add_new_habit_button)
            )
            return True
        except TimeoutException:
            return False
