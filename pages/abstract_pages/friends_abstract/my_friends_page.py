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
        "tab_my_friends": (By.XPATH, "//a[contains(., 'My friends')]"),
        "tab_find_friend": (By.XPATH, "//a[contains(., 'Find a friend')]"),
        "tab_friend_requests": (By.XPATH, "//a[contains(., 'Friend requests')]"),
        "friend_cards": (By.CSS_SELECTOR, ".friends-list .user-card")
    }

    back_btn: CustomWebElement
    search_input: CustomWebElement
    tab_my_friends: CustomWebElement
    tab_find_friend: CustomWebElement
    tab_friend_requests: CustomWebElement

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
        tab_name = tab_name.lower()

        if tab_name == "my friends":
            self.tab_my_friends.click()
        elif tab_name == "find a friend":
            self.tab_find_friend.click()
        elif tab_name == "friend requests":
            self.tab_friend_requests.click()
        else:
            raise ValueError(f"Unknown tab: {tab_name}")

    @allure.step("Get friend items")
    def get_friend_items(self) -> list[FriendItemComponent]:
        """Get friend items"""
        elements = self.driver.find_elements(*self.locators["friend_cards"])
        return [FriendItemComponent(el) for el in elements]
