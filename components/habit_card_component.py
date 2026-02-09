"""
habit card component
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from utils.types import Locators


class HabitCardComponent:
    """Responsible for one difficult habit on the list"""

    title: Locators = (By.CSS_SELECTOR, ".description .second-row")

    checkbox: Locators = (By.XPATH, ".//div/div[2]/button")

    edit_icon: Locators = (By.XPATH, ".//div/div[1]/div[1]/button")

    def __init__(self, root: WebElement):
        self.root = root

    def get_title(self) -> str:
        """get title"""
        return self.root.find_element(*self.title).text

    def mark_as_done(self):
        """mark habit as done"""
        self.root.find_element(*self.checkbox).click()

    def click_edit(self):
        """click edit button"""
        self.root.find_element(*self.edit_icon).click()
