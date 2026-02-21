"""
Habit page
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    @allure.step("Navigating to the About Us page from My Habit page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        from pages.about_us_page import AboutUsPage # pylint: disable=import-outside-toplevel
        self.header.click_about_us_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)

    @allure.step("Checking if My Habit page is opened")
    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.is_visible(self.my_habits_tab_locator)
