"""This module contains the AllFriendsPage class,
which represents the Friend page with All friends tab."""
from typing import List

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

        "cards": (By.CSS_SELECTOR, "div.friend-item-wrapper", List[FriendCardComponent]),
        "default_text": (By.XPATH, ".//h3[@class='no-friends']"),
        "content_block": (By.CSS_SELECTOR, "div.mat-mdc-tab-body-wrapper")
    }

    cards: list[FriendCardComponent]
    default_text: CustomWebElement
    content_block: CustomWebElement

    @allure.step("Get all friend cards on the All friends tab on User profile page")
    def get_cards_list(self) -> list:
        """Get all friend cards on the all friends tab."""
        self.get_wait().until(EC.visibility_of(self.content_block))
        return self.cards


    @allure.step("Get the text on the All friends tab without friends on User profile page")
    def get_default_text(self) -> str:
        """Get the text on the all friends tab without friends."""
        return self.get_wait().until(EC.visibility_of(self.default_text)).text
