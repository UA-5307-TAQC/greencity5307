"""My friends page"""

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.friend_item_component import FriendItemComponent


class FriendsPage(BasePage):
    """Friends page"""

    back_btn = (By.CSS_SELECTOR, ".button-link")
    search_input = (By.CSS_SELECTOR, ".searchForm input.search")
    tab_my_friends = (By.XPATH, "//a[contains(., 'My friends')]")
    tab_find_friend = (By.XPATH, "//a[contains(., 'Find a friend')]")
    tab_friend_requests = (By.XPATH, "//a[contains(., 'Friend requests')]")
    friend_cards = (By.CSS_SELECTOR, ".friends-list .user-card")

    def click_back(self):
        """Click back"""
        self.driver.find_element(*self.back_btn).click()

    def search_friend(self, text):
        """Search friends"""
        search_field = self.driver.find_element(*self.search_input)
        search_field.clear()
        search_field.send_keys(text)

    def select_tab(self, tab_name: str):
        """Select tab"""
        if tab_name.lower() == "my friends":
            self.driver.find_element(*self.tab_my_friends).click()
        elif tab_name.lower() == "find a friend":
            self.driver.find_element(*self.tab_find_friend).click()
        elif tab_name.lower() == "friend requests":
            self.driver.find_element(*self.tab_friend_requests).click()
        else:
            raise ValueError(f"Unknown tab: {tab_name}")

    def get_friend_items(self):
        """Get friend items"""
        elements = self.driver.find_elements(*self.friend_cards)
        return [FriendItemComponent(el) for el in elements]
