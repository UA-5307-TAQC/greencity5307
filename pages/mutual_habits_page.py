"""This module contains the MutualHabits class,which represents the event page of a website.
 It inherits from the BasePage class and provides specific locators and methods
for interacting with the event page elements."""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from components.mutual_habits_component import MutualHabitsComponent
from pages.base_page import BasePage
from utils.types import Locators



class MutualHabitsPage(BasePage):
    """ Page for mutual habits. """

    root_locator: Locators = (By.ID, "mat-tab-content-8-4")
    page_title_locator: Locators = (By.CSS_SELECTOR, ".gallery.ng-star-inserted")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


        try:
            root_element = self.driver.find_element(*self.root_locator)
            self.habits_list = MutualHabitsComponent(root_element)
        except NoSuchElementException:

            self.habits_list = None

    def get_title_text(self) -> str:
        """Get page title."""
        return self.driver.find_element(*self.page_title_locator).text
