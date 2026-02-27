"""This module contains the FriendsAbstractPage class,
which represents the friends_abstract page of a website."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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
        "friend_tabs": (By.CSS_SELECTOR, ".friend-tabs")
    }

    def go_back_to_profile(self):
        """Clicks the back to profile button."""
        self.back_to_profile_button.wait_and_click()

    def search_friend(self, text: str):
        """Enters text into the search input."""
        self.search_input.send_keys(text)

    def is_page_loaded(self) -> bool:
        """Checks if the page is loaded by verifying the visibility of the title and friend tabs."""
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of(self.search_input)
        )
        return True

    @allure.step("Navigating to the About Us page from Friends page")
    def go_to_about_us(self):
        """Navigate to About Us page."""
        from pages.common_pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel

        self.header.click_about_us_link()

        WebDriverWait(self.driver, 10).until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)
