"""
user habit card component
"""
from selenium.webdriver.common.by import By
from components.base_component import BaseComponent
from utils.types import Locators


class UserHabitCardComponent(BaseComponent):
    """Responsible for one difficult habit on the list"""

    title: Locators = (By.CSS_SELECTOR, ".description .second-row")

    checkbox: Locators = (By.XPATH, ".//div/div[2]/button")

    edit_icon: Locators = (By.XPATH, ".//div/div[1]/div[1]/button")
