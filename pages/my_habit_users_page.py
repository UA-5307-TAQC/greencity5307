""" Habit components """
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.types import Locators


class MyHabitUsersPage(BaseComponent): # FriendAbstract required
    """ Habit user components """
    stars: Locators = (By.CSS_SELECTOR, ".habit-header .stars")
    tags: Locators = (By.CSS_SELECTOR, ".habit-info .tags")
    all_titles: Locators = (By.XPATH, "//app-habits-gallery-view//h2")
    more_buttons:Locators = (By.CSS_SELECTOR, ".habit-action-wrp .secondary-global-button")
    added_habit_button:Locators = (By.CSS_SELECTOR,".habit-action-wrp .primary-global-button")
