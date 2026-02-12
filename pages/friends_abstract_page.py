"""This module contains the FriendsAbstractPage class,
which represents the friends_abstract page of a website."""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage
from utils.types import Locators


class FriendsAbstractPage(BasePage):
    """Page object for the friends_abstract page."""

    back_to_profile_button = (By.CSS_SELECTOR, ".button-link")
    search_input = (By.CSS_SELECTOR, ".search")
    friend_tabs = (By.CSS_SELECTOR, ".friend-tabs")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.main_header = self.driver.find_element(*self.main_header_locator)
        self.main_footer = self.driver.find_element(*self.main_footer_locator)

    def go_back_to_profile(self):
        self.click(self.back_to_profile_button)

    def search_friend(self, text: str):
        self.find(self.search_input).send_keys(text)

    def is_page_loaded(self):
        return self.find(self.friend_tabs).is_displayed()

