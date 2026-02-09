"""Mutual Friends component."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent


class MutualFriendsComponent(BaseComponent):
    """
    Component for Mutual Friends Page
    """

    empty_message = (By.CSS_SELECTOR,
                     "#mat-tab-content-9-4 > div > div.img-absent.ng-star-inserted > h3")
    friends_card = (By.CSS_SELECTOR,
                    "#mat-tab-content-9-4 > div > div.friends-list.ng-star-inserted")

    def is_empty_state_displayed(self) -> bool:
        """Check if the empty message is displayed."""
        try:
            message = self.find_element(self.empty_message)
            return message.is_displayed()
        except NoSuchElementException:
            return False

    def get_empty_state_text(self) -> str:
        """Get empty message text."""
        try:
            return self.get_text(self.empty_message)
        except NoSuchElementException:
            return ""

    def get_friends_count(self) -> int:
        """Return number of founded friends."""
        if self.is_empty_state_displayed():
            return 0

        friends = self.find_elements(self.friends_card)
        return len(friends)
