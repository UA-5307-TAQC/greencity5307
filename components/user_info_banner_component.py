"""This module contains UserInfoBannerComponent, that
represent user info banner on the user's page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from components.base_component import BaseComponent


class UserInfoBannerComponent(BaseComponent):
    """UserInfoBannerComponent class."""
    friend_btn_locator = (By.CSS_SELECTOR, ".friend-btn")

    def click_add_friend(self):
        """Clicks 'Add friend' button."""
        add_friend_button = self.root.find_element(*self.friend_btn_locator)
        if add_friend_button.text.strip() == "Add friend":
            add_friend_button.click()

    def click_cancel_request(self):
        """Clicks 'Cancel request' button."""
        cancel_request_button = self.root.find_element(*self.friend_btn_locator)
        if cancel_request_button.text.strip() == "Cancel request":
            cancel_request_button.click()

    def is_loaded(self):
        """Verifies that the component is loaded."""
        try:
            friend_button = self.root.find_element(*self.friend_btn_locator)
            WebDriverWait(self.root.parent, 5).until(
                EC.element_to_be_clickable(friend_button)
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
