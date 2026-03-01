"""This module contains the page object for the find_friend page."""
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.abstract_pages.friends_abstract.friends_abstract_page \
    import FriendsAbstractPage

from components.abstract_pages_components.friends_components \
    .friend_card_component import FriendCardComponent


class FindFriendPage(FriendsAbstractPage):
    """Page object class for the Find Friend page."""

    locators = {
        "friend_card": (By.CSS_SELECTOR, ".user-card", FriendCardComponent)
    }

    _friend_card_by_name_pattern = ("//div[contains(@class, 'user-card')]"
                                    "[.//p[contains(@class, 'friend-name') "
                                    "and contains(text(), '{}')]]")

    def get_friend_card_by_name(self, name: str):
        """Finds a friend card element by the friend's name."""
        formatted_pattern = self._friend_card_by_name_pattern.format(name)
        friend_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        return FriendCardComponent(friend_card_element)

    def is_page_loaded(self) -> bool:
        try:
            self.get_wait().until(
                EC.visibility_of_element_located(self.locators["friend_card"])
            )
            return True
        except TimeoutException:
            return False
