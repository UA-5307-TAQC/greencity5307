"""This module contains the AllFriendsPage class,
which represents the Friend page with All friends tab."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.abstract_pages_components.friends_components \
    .friend_card_component import FriendCardComponent
from pages.abstract_pages.friend_abstract_users.friend_abstract_page \
    import FriendAbstractPage
from utils.custom_web_element import CustomWebElement


class AllFriendsPage(FriendAbstractPage):
    """Class for the all friends tab of Friend page."""

    locators = {
        "card_roots": (By.CSS_SELECTOR, "div.friend-item-wrapper"),
        "default_text": (By.XPATH, ".//h3[@class='no-friends']")
    }

    card_roots: list
    default_text: CustomWebElement

    @allure.step("Get all friend cards on the All friends tab on User profile page")
    def get_cards_list(self) -> list:
        """Get all friend cards on the all friends tab."""
        found_card_roots = self.resolve_list("card_roots")
        friend_cards = []
        for card_root in found_card_roots:
            friend_cards.append(FriendCardComponent(card_root))
        return friend_cards


    @allure.step("Get the text on the All friends tab without friends on User profile page")
    def get_default_text(self) -> str:
        """Get the text on the all friends tab without friends."""
        return self.get_wait().until(EC.visibility_of(self.default_text)).text
