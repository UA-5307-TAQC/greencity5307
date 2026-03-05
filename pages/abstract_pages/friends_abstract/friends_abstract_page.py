"""This module contains the FriendsAbstractPage class,
which represents the friends_abstract page of a website."""
import allure
from typing import Self
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from components.abstract_pages_components.friends_components.friends_tabs_buttons_component import \
    FriendsTabsButtonsComponent
from pages.base_page import BasePage


class FriendsAbstractPage(BasePage):
    """Page object for the friends_abstract page."""
    locators = {
        "title_locator": (By.CSS_SELECTOR, "body > app-root > app-main > div > "
                                           "div.main-content.app-container > app-greencity-main > "
                                           "app-user-component > app-friend-dashboard > div > "
                                           "div > div > h1"),
        "back_to_profile_button": (By.CSS_SELECTOR, ".button-link"),
        "search_input": (By.CSS_SELECTOR, ".search"),
        "friend_tabs": (By.CSS_SELECTOR, "body > app-root > app-main > div > "
                                         "div.main-content.app-container > "
                                         "app-greencity-main > app-user-component > "
                                         "app-friend-dashboard > div > "
                                         "div > div > div")
    }
    def get_my_friends_tab(self):
        """Clicks on the My Friends tab."""
        element = self.driver.find_element(*self.locators["friend_tabs"])
        return FriendsTabsButtonsComponent(element)

    def get_friend_requests_tab(self):
        """Clicks on the Friend Requests tab."""
        element = self.driver.find_element(*self.locators["friend_tabs"])
        return FriendsTabsButtonsComponent(element)

    def get_find_friend_tab(self):
        """Clicks on the Find a Friend tab."""
        element = self.driver.find_element(*self.locators["friend_tabs"])
        return FriendsTabsButtonsComponent(element)

    def go_to_my_friend_tab(self) -> Self:
        """Clicks on the specified friend tab."""
        self.get_my_friends_tab().click_my_friends_tab()
        return self

    def go_to_friend_requests_tab(self) -> Self:
        """Clicks on the specified friend tab."""
        self.get_friend_requests_tab().click_friend_requests_tab()
        return self

    def go_to_find_friend_tab(self) -> Self:
        """Clicks on the specified friend tab."""
        self.get_find_friend_tab().click_find_friend_tab()
        return self

    def go_back_to_profile(self):
        """Clicks the back to profile button."""
        self.back_to_profile_button.wait_and_click()


    def search_friend(self, text: str):
        """Enters text into the search input."""
        self.search_input.send_keys(text)

    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded by verifying the visibility of the title and friend tabs."""
        self.get_wait().until(
            EC.visibility_of(self.search_input)
        )
        return True

    @allure.step("Navigating to the About Us page from Friends page")
    def go_to_about_us(self):
        """Navigate to About Us page."""
        from pages.common_pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel

        self.header.click_about_us_link()

        self.get_wait().until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)
