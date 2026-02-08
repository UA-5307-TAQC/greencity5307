"""
Habit components
"""
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class MyHabitComponent(BaseComponent):#MySpaceAbstract required
    """ Habit component """
    habit_cards_list = (By.TAG_NAME, "app-one-habit")
    add_new_habit_button: Locators = (By.XPATH, "//*[@id='create-button-new-habit']/span")
