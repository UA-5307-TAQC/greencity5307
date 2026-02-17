"""
Habit page
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.user_habit_card_component import UserHabitCardComponent
from pages.my_space_abstract_page import MySpaceAbstractPage
from utils.types import Locators


class MyHabitPage(MySpaceAbstractPage):
    """ Habit page """
    habit_cards_list: Locators = (By.TAG_NAME, "app-one-habit")
    habit_card_for_test: Locators = (By.XPATH, "(//app-one-habit)[1]")
    add_new_habit_button: Locators = (By.XPATH, ".//*[@id='create-button-new-habit']/span")

    def __init__(self, driver):
        super().__init__(driver)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_any_elements_located(self.habit_cards_list)
        )

    def get_habit_card(self) -> UserHabitCardComponent:
        """Get the habit cards list"""
        element = self.find(self.habit_card_for_test)
        return UserHabitCardComponent(element)
