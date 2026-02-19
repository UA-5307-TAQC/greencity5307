"""This module contains the page object for the find_friend page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.friends_abstract_page import FriendsAbstractPage

from components.friend_card_component import FriendCardComponent


class FindFriendPage(FriendsAbstractPage):
    """Page object class for the Find Friend page."""

    _friend_card_by_name_pattern = ("//div[contains(@class, 'user-card')]"
                                    "[.//p[contains(@class, 'friend-name') "
                                    "and contains(text(), '{}')]]")
    friend_card_item = (By.CSS_SELECTOR, ".user-card")
    _snack_bar_message = (By.CSS_SELECTOR, "div[matsnackbarlabel]")

    def get_friend_card_by_name(self, name: str):
        """Finds a friend card element by the friend's name."""
        formatted_pattern = self._friend_card_by_name_pattern.format(name)
        friend_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        return FriendCardComponent(friend_card_element)

    def is_page_loaded(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.friend_card_item)
            )
            return True
        except TimeoutException:
            return False

    def get_friend_request_sent_msg(self):
        """Getting text from snack bar message."""
        try:
            snack_bar_element = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self._snack_bar_message)
            )
            return snack_bar_element.text.strip()
        except TimeoutException:
            return ""
