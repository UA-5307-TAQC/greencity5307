"""
habit card component
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class HabitCardComponent:
    """Responsible for one difficult habit on the list"""

    title = (By.CSS_SELECTOR, ".description .second-row")
    checkbox = (By.CSS_SELECTOR, "//*[@id='mat-tab-content-8-0']/div/div/div/div[2]/app-one-habit[1]/div/div[2]/button")
    edit_icon = (By.XPATH, "//*[@id='mat-tab-content-8-0']/div/div/div/div[2]/app-one-habit[1]/div/div[1]/div[1]/button")

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