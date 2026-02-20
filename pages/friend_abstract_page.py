"""This module contains the FriendAbstractPage class."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.user_info_banner_component import UserInfoBannerComponent


class FriendAbstractPage(BasePage):
    """Page object for the Friend Abstract (other user) page."""
    user_info_banner_locator = (By.CSS_SELECTOR, ".side-bar")

    def __init__(self, driver):
        super().__init__(driver)
        self._user_info_banner_root = self.driver.find_element(*self.user_info_banner_locator)
        self.user_info_banner = UserInfoBannerComponent(self._user_info_banner_root)
