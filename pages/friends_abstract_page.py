"""This module contains the FriendsAbstractPage class,
which represents the friends_abstract page of a website."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.types import Locators


class FriendsAbstractPage(BasePage):
    """Page object for the friends_abstract page."""

    back_to_profile_button: Locators = (By.CSS_SELECTOR, ".button-link")
    search_input: Locators = (By.CSS_SELECTOR, ".search")
    friend_tabs: Locators = (By.CSS_SELECTOR, ".friend-tabs")

    def go_back_to_profile(self):
        """Clicks the back to profile button."""
        self.click(self.back_to_profile_button)

    def search_friend(self, text: str):
        """Enters the specified text into the search input field."""
        self.find(self.search_input).send_keys(text)

    def is_page_loaded(self):
        """Checks if the page is loaded by verifying the presence of the friend tabs."""
        return self.find(self.friend_tabs).is_displayed()
