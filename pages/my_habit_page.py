"""
Habit page
"""
from selenium.webdriver.common.by import By

from pages.my_space_abstract_page import MySpaceAbstractPage
from utils.types import Locators


class MyHabitPage(MySpaceAbstractPage):
    """ Habit page """
    habit_cards_list: Locators = (By.TAG_NAME, "app-one-habit")
    add_new_habit_button: Locators = (By.XPATH, "//*[@id='create-button-new-habit']/span")
