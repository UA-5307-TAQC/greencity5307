"""Mutual Friends component."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class MutualFriendsComponent(BaseComponent):
    """
    Component for Mutual Friends Page
    """

    locators = {
        "empty_message": (By.CSS_SELECTOR, "div > div.img-absent.ng-star-inserted > h3"),
        "friends_card": (By.CSS_SELECTOR, "div > div.friends-list.ng-star-inserted")
    }

    def is_empty_state_displayed(self) -> bool:
        """Check if the empty message is displayed."""
        try:
            return self.empty_message.is_displayed()
        except NoSuchElementException:
            return False

    def get_empty_state_text(self) -> str:
        """Get empty message text."""
        try:
            return self.empty_message.text
        except NoSuchElementException:
            return ""

    def get_friends_count(self) -> int:
        """Return the number of friends found."""
        if self.is_empty_state_displayed():
            return 0

        friends = self.resolve_list("friends_card")
        return len(friends)
