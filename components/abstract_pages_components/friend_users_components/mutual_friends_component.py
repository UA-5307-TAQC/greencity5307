"""Mutual Friends component."""

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement



class MutualFriendsComponent(BaseComponent):
    """
    Component for Mutual Friends Page
    """

    locators = {
        "empty_message": (By.CSS_SELECTOR, "div > div.img-absent.ng-star-inserted > h3"),
        "friends_card": (By.CSS_SELECTOR, "div > div.friends-list.ng-star-inserted"),
        "friend_names": (By.CSS_SELECTOR, ".friend-name"),
        "friend_avatars": (By.XPATH, ".//app-user-profile-image[contains(@class, 'friend-img')]")

    }

    friend_cards: list[CustomWebElement]
    friend_names: list[CustomWebElement]
    friend_avatars: list[CustomWebElement]

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

    def get_all_friend_names(self) -> list[str]:
        """Return all friends names."""
        elements = self.driver.find_elements(*self.locators["friend_names"])
        return [elem.text.strip() for elem in elements if elem.text.strip()]

    def is_first_friend_avatar_visible(self) -> bool:
        """Check if the first friend avatar was visible."""
        elements = self.driver.find_elements(*self.locators["friend_avatars"])
        if not elements:
            return False
        return elements[0].is_displayed()
