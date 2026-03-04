"""This module contains UserInfoBannerComponent, that
represent user info banner on the user's page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.base_component import BaseComponent

from utils.custom_web_element import CustomWebElement


class UserInfoBannerComponent(BaseComponent):
    """UserInfoBannerComponent class."""
    locators = {
        "friend_btn": (By.CSS_SELECTOR, ".friend-btn")
    }

    friend_btn: CustomWebElement

    def click_add_friend(self):
        """Clicks 'Add friend' button."""
        if self.friend_btn.text.strip() == "Add friend":
            self.friend_btn.wait_and_click()

    def click_cancel_request(self):
        """Clicks 'Cancel request' button."""
        if self.friend_btn.text.strip() == "Cancel request":
            self.friend_btn.wait_and_click()

    def is_loaded(self):
        """Verifies that the component is loaded."""
        try:
            locator_tuple = (By.CSS_SELECTOR, ".friend-btn")
            self.get_wait().until(
                EC.element_to_be_clickable(locator_tuple)
            )
            return True
        except TimeoutException:
            return False

    def get_friend_button_text(self):
        """Gets text from the friend button."""
        actual_friend_button = self.root.find_element(*self.friend_btn_locator)
        WebDriverWait(self.root.parent, 5).until(
            EC.element_to_be_clickable(actual_friend_button)
        )
        return actual_friend_button.text.strip()
