"""My friends page"""
import allure

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.abstract_pages_components.friends_components \
    .friend_item_component import FriendItemComponent
from utils.custom_web_element import CustomWebElement


class FriendsPage(BasePage):
    """Friends page"""

    locators = {
        "back_btn": (By.CSS_SELECTOR, ".button-link"),
        "search_input": (By.CSS_SELECTOR, ".searchForm input.search"),
        "tab_my_friends": (By.XPATH, "//a[contains(., 'My friends') or contains(., 'Мої друзі')]"),
        "tab_find_friend": (By.XPATH, "//a[contains(., 'Find a friend') "
                                      "or contains(., 'Знайти друга')]"),
        "tab_friend_requests": (By.XPATH, "//a[contains(., 'Friend requests') "
                                          "or contains(., 'Запити в друзі')]"),
        "friend_cards": (By.CSS_SELECTOR, ".friends-list .user-card", list[FriendItemComponent]),
    }

    back_btn: CustomWebElement
    search_input: CustomWebElement
    tab_my_friends: CustomWebElement
    tab_find_friend: CustomWebElement
    tab_friend_requests: CustomWebElement
    friend_cards: list[FriendItemComponent]

    @allure.step("Click Back button")
    def click_back(self):
        """Click back"""
        self.back_btn.click()

    @allure.step("Search friend: {text}")
    def search_friend(self, text: str):
        """Search friends"""
        self.search_input.clear()
        self.search_input.send_keys(text)

    @allure.step("Select tab: {tab_name}")
    def select_tab(self, tab_name: str):
        """Select tab"""
        from pages.abstract_pages.friends_abstract.find_friend_page import FindFriendPage  # pylint: disable=import-outside-toplevel
        from pages.abstract_pages.friends_abstract.friend_requests_page import FriendRequestsPage  # pylint: disable=import-outside-toplevel
        tab_name = tab_name.strip().lower()
        page = None

        if tab_name in ("my friends", "мої друзі"):
            self.tab_my_friends.wait_and_click()
        elif tab_name in ("find a friend", "знайти друга"):
            self.tab_find_friend.wait_and_click()
            page = FindFriendPage(self.driver)
        elif tab_name in ("friend requests", "запити в друзі"):
            self.tab_friend_requests.wait_and_click()
            page = FriendRequestsPage(self.driver)
        else:
            raise ValueError(f"Unknown tab: {tab_name}")
        return page

    @allure.step("Get friend items")
    def get_friend_items(self) -> list[FriendItemComponent]:
        """Get friend items"""
        return self.friend_cards

    @allure.step("Check My Friends page is loaded")
    def is_page_loaded(self) -> bool:
        """Checks if the 'My friends' page is loaded."""
        return self._is_loaded_indicator(self.locators["search_input"][:2])
