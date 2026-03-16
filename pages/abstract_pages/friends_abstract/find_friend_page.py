"""This module contains the page object for the find_friend page."""
from typing import List
import allure

from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.abstract_pages.friends_abstract.friends_abstract_page \
    import FriendsAbstractPage

from components.abstract_pages_components.friends_components \
    .friend_card_component import FriendCardComponent


class FindFriendPage(FriendsAbstractPage):
    """Page object class for the Find Friend page."""

    locators = {
        "friend_card": (By.CSS_SELECTOR, ".user-card", FriendCardComponent),
        "cards": (By.CSS_SELECTOR, "div.friend-item-wrapper", List[FriendCardComponent])
    }

    friend_card: FriendCardComponent
    cards: list[FriendCardComponent]

    _friend_card_by_name_pattern = ("//div[contains(@class, 'user-card')]"
                                    "[.//p[contains(@class, 'friend-name') "
                                    "and contains(text(), '{}')]]")

    def get_friend_card_by_name(self, name: str):
        """Finds a friend card element by the friend's name."""
        formatted_pattern = self._friend_card_by_name_pattern.format(name)
        friend_card_element = self.driver.find_element(By.XPATH, formatted_pattern)
        return FriendCardComponent(friend_card_element)

    def is_page_loaded(self) -> bool:
        """Verifies that Find Friend page loads by checking any friend card."""
        try:
            self.get_wait().until(EC.visibility_of(self.cards))
            return True
        except TimeoutException:
            return False

    def get_first_card(self) -> FriendCardComponent | None:
        """Returns the first friend card if it exists."""
        try:
            return self.friend_card
        except NoSuchElementException:
            return None


    def wait_for_list_to_load(self) -> None:
        """Waits until at least one friend card is visible on the page."""
        self.get_wait().until(EC.visibility_of_element_located(self.locators["cards"][:2]))


    @allure.step("Get all friend cards on the Find Friend page")
    def get_all_friend_cards(self) -> list[FriendCardComponent]:
        """Returns all friend cards on the page."""
        self.wait_for_list_to_load()
        return self.cards
