"""This module contains the MutualFriendsPage class and its methods."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from components.mutual_friends_component import MutualFriendsComponent



class MutualFriendsPage(BasePage):
    """
    Page that shows mutual friends page.
    """

    locators = {
        "root": (By.XPATH, "(//*[contains(@class, 'mdc-tab')]/span[2]/span)[5]"),
        "page_title": (By.CSS_SELECTOR, ".friends-list.ng-star-inserted", MutualFriendsComponent)
    }


    def has_mutual_friends(self) -> bool:
        """Check if the mutual friends page is visible."""
        locator = self.locators["page_title"][:2]
        return self.is_visible(locator)

    def get_title_text(self) -> str:
        """Get page title."""
        return self.page_title.text
