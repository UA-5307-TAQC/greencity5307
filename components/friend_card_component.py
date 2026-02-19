"""This module contains the FriendCardComponent class,
 which represents the friend card on a web page."""

import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from components.base_component import BaseComponent
from utils.types import Locators


class FriendCardComponent(BaseComponent):
    """Component class for the friend card on a web page."""
    friend_name_locator: Locators = (By.CSS_SELECTOR, "p.friend-name")
    friend_city_locator: Locators = (By.CSS_SELECTOR, "p.friend-city")
    add_friend_btn_locator: Locators = (By.CSS_SELECTOR, "button#addFriend")

    def __init__(self, root: WebElement):
        super().__init__(root)
        self.friend_name = self.root.find_element(*self.friend_name_locator)
        self.friend_city = self.root.find_element(*self.friend_city_locator)
        self.add_friend_btn = self.root.find_element(*self.add_friend_btn_locator)

    @allure.step("Get a friend name and city from a Friend card")
    def get_friend_info(self) -> dict:
        """Get a friend name and city from a friend card."""
        friend_info = {
            "name": self.friend_name.text,
            "city": self.friend_city.text
            }
        return friend_info

    @allure.step("Click Add friend button on a Friend card")
    def click_add_friend_btn(self):
        """Click Add friend button."""
        actual_friend_button = self.root.find_element(*self.add_friend_btn_locator)
        if actual_friend_button.text.strip() == "Add friend":
            actual_friend_button.click()

    def click_cancel_request_btn(self):
        """Click Cancel request button."""
        actual_friend_button = self.root.find_element(*self.add_friend_btn_locator)
        if actual_friend_button.text.strip() == "Cancel request":
            actual_friend_button.click()

    @allure.step("Click on a Friend card")
    def click_friend_card(self):
        """Click on a friend card."""
        self.root.click()
        from pages.all_habits_user_page import AllHabitsUsersPage  # pylint: disable=import-outside-toplevel
        return AllHabitsUsersPage(self.root.parent)

    def get_friend_button_text(self):
        """Gets text from the friend button."""
        actual_friend_button = self.root.find_element(*self.add_friend_btn_locator)
        WebDriverWait(self.root.parent, 5).until(
            EC.element_to_be_clickable(actual_friend_button)
        )
        return actual_friend_button.text.strip()
