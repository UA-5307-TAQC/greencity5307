"""This module contains the page object for the find_friend page."""
from selenium.webdriver.common.by import By

from pages.abstract_pages.friends_abstract.friends_abstract_page \
    import FriendsAbstractPage

from components.abstract_pages_components.friends_components \
    .friend_card_component import FriendCardComponent


class FindFriendPage(FriendsAbstractPage):
    """Page object class for the Find Friend page."""

    _friend_card_by_name_pattern = ("//div[contains(@class, 'user-card')]"
                                    "[.//p[contains(@class, 'friend-name') "
                                    "and contains(text(), '{}')]]")

    def get_friend_card_by_name(self, name: str):
        """Finds a friend card element by the friend's name."""
        formatted_pattern = self._friend_card_by_name_pattern.format(name)
        friend_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        return FriendCardComponent(friend_card_element)
