"""
Habit components
"""

from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
from components.habit_card_component import HabitCardComponent
from utils.types import Locators


class MyHabitComponent(BaseComponent):#MySpaceAbstract required
    """ Habit component """
    habit_cards_list = (By.TAG_NAME, "app-one-habit")
    add_new_habit_button: Locators = (By.XPATH, "//*[@id='create-button-new-habit']/span")
    def get_all_habits(self):
        """
        find all habit cards and remake to list elements HabitCardComponent
        """
        elements = self.driver.find_elements(*self.habit_cards_list)

        return [HabitCardComponent(element) for element in elements]

    def get_habit_by_name(self, name: str):
        """find habit by name"""
        for habit in self.get_all_habits():
            if habit.get_habit_title() == name:
                return habit
        raise Exception(f"Habit '{name}' not found")

