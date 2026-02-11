"""This module contains the AllFriendsPage class,
which represents the Friend page with All friends tab."""

from selenium.webdriver.common.by import By

from pages.friend_page_abstract import FriendPageAbstract
from components.friend_card_component import FriendCardComponent
from utils.types import Locators


class AllFriendsPage(FriendPageAbstract):
    """Class for the all friends tab of Friend page."""
    cards_root_locator: Locators = (By.CLASS_NAME, "friend-item-wrapper")
    default_text_locator: Locators = (By.XPATH, ".//h3[@class='no-friends']")


    def __init__(self, driver):
        super().__init__(driver)
        self.card_roots = self.driver.find_elements(*self.cards_root_locator)
        self.default_text = self.driver.find_element(*self.default_text_locator)


    def get_cards_list(self) -> list:
        """Get all friend cards on the all friends tab."""
        friend_cards = []
        for card_root in self.card_roots:
            friend_cards.append(FriendCardComponent(card_root))
        return friend_cards


    def get_default_text(self) -> str:
        """Get the text on the all friends tab without friends."""
        return self.default_text.text
