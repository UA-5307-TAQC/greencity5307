"""This module contains the FriendAbstractPage class."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from components.abstract_pages_components.friend_users_components.user_info_banner_component \
    import UserInfoBannerComponent


class FriendAbstractPage(BasePage):
    """Page object for the Friend Abstract (other user) page."""

    locators = {
        "user_info_banner": (By.CSS_SELECTOR, ".side-bar", UserInfoBannerComponent)
    }

    user_info_banner: UserInfoBannerComponent
