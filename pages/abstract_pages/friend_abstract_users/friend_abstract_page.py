"""This module contains the FriendAbstractPage class."""
import allure

from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from pages.base_page import BasePage
from components.abstract_pages_components.friend_users_components.user_info_banner_component \
    import UserInfoBannerComponent
from utils.custom_web_element import CustomWebElement


class FriendAbstractPage(BasePage):
    """Page object for the Friend Abstract (other user) page."""

    locators = {
        "user_info_banner": (By.CSS_SELECTOR, ".side-bar", UserInfoBannerComponent),
        "all_habits_tab": (By.XPATH, "(.//div[@role='tab'])[1]"),
        "mutual_habits_tab": (By.XPATH, "(.//div[@role='tab'])[2]"),
        "my_habits_tab": (By.XPATH, "(.//div[@role='tab'])[3]"),
        "all_friends_tab": (By.XPATH, "(.//div[@role='tab'])[4]"),
        "mutual_friends_tab": (By.XPATH, "(.//div[@role='tab'])[5]")
    }

    user_info_banner: UserInfoBannerComponent
    all_habits_tab: CustomWebElement
    mutual_habits_tab: CustomWebElement
    my_habits_tab: CustomWebElement
    all_friends_tab: CustomWebElement
    mutual_friends_tab: CustomWebElement


    @allure.step("Click on the All Friends tab")
    def click_all_friends_tab(self) -> "AllFriendsPage":
        """Click the All Friends tab."""
        from pages.abstract_pages.friend_abstract_users.all_friends_page import (  # pylint: disable=import-outside-toplevel
            AllFriendsPage,
        )
        self.all_friends_tab.wait_and_click()
        return AllFriendsPage(self.driver)


    @allure.step("Check if user info banner is visible")
    def has_user_banner(self) -> bool:
        """Verifies if the driver is currently on the expected page by checking
        for a user banner."""
        try:
            self.get_wait().until(EC.visibility_of(self.user_info_banner))
            return True
        except (NoSuchElementException, TimeoutException):
            return False
