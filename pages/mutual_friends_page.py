"""This module contains the MutualFriendsPage class and its methods."""
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from components.mutual_friends_component import MutualFriendsComponent
from utils.types import Locators



class MutualFriendsPage(BasePage):
    """
    Page that shows mutual friends page.
    """

    root_locator: Locators = (By.ID, "mat-tab-content-6-4")
    page_title_locator: Locators = (By.CSS_SELECTOR, ".friends-list.ng-star-inserted")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


        try:
            root_element = self.driver.find_element(*self.root_locator)
            self.friends_list = MutualFriendsComponent(root_element)
        except NoSuchElementException:

            self.friends_list = None

    def get_title_text(self) -> str:
        """Get page title."""
        return self.driver.find_element(*self.page_title_locator).text
