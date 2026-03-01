"""This module contains the FriendCardComponent class,
 which represents the friend card on a web page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.abstract_pages.friend_abstract_users.all_habits_page import AllHabitsPage
from components.base_component import BaseComponent
from utils.custom_web_element import CustomWebElement


class FriendCardComponent(BaseComponent):
    """Component class for the friend card on a web page."""

    locators = {
        "friend_name": (By.CSS_SELECTOR, "p.friend-name"),
        "friend_city": (By.CSS_SELECTOR, "p.friend-city"),
        "add_friend_btn": (By.CSS_SELECTOR, ".friend-btn")
    }

    friend_name: CustomWebElement
    friend_city: CustomWebElement
    add_friend_btn: CustomWebElement

    @allure.step("Get a friend name and city from a Friend card")
    def get_friend_info(self) -> dict:
        """Get a friend name and city from a friend card."""
        friend_info = {
            "name": self.get_wait().until(EC.visibility_of(self.friend_name)).text,
            "city": self.get_wait().until(EC.visibility_of(self.friend_city)).text
            }
        return friend_info


    @allure.step("Click Add friend button on a Friend card")
    def click_add_friend_btn(self):
        """Click Add friend button."""
        self.add_friend_btn.wait_and_click()


    @allure.step("Click on a Friend card")
    def click_friend_card(self):
        """Click on a friend card."""
        CustomWebElement(self.root).wait_and_click()
        return AllHabitsPage(self.driver)
