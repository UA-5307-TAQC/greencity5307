"""
Habit page
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.my_space_abstract_page import MySpaceAbstractPage
from utils.types import Locators


class MyHabitPage(MySpaceAbstractPage):
    """ Habit page """
    habit_cards_list: Locators = (By.TAG_NAME, "app-one-habit")
    add_new_habit_button_locator: Locators = (By.XPATH,
                                              ".//span[text()='Add New Habit']/..")


    def __init__(self, driver):
        super().__init__(driver)
        self.add_new_habit_button = self.driver.find_element(*self.add_new_habit_button_locator)

    def wait_page_loaded(self):
        """Wait for the My Habit page to load."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.add_new_habit_button_locator)
        )

    @allure.step("Clicking Add New Habit button on the My Habit page")
    def click_add_new_habit_button(self):
        """Click on Add New Habit button."""
        from pages.all_habits_page import AllHabitPage # pylint: disable=import-outside-toplevel
        self.add_new_habit_button.click()
        return AllHabitPage(self.driver)

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
