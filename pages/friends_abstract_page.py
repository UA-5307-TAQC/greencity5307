"""This module contains the FriendsAbstractPage class,
which represents the friends_abstract page of a website."""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.types import Locators


class FriendsAbstractPage(BasePage):
    """Page object for the friends_abstract page."""
    title_locator: Locators = (By.CSS_SELECTOR,
                               "body > app-root > app-main > div > "
                               "div.main-content.app-container > "
                               "app-greencity-main > app-user-component > "
                               "app-friend-dashboard > div > div > div > h1")
    back_to_profile_button: Locators = (By.CSS_SELECTOR, ".button-link")
    search_input: Locators = (By.CSS_SELECTOR, ".search")
    friend_tabs: Locators = (By.CSS_SELECTOR, ".friend-tabs")

    def go_back_to_profile(self):
        """Clicks the back to profile button."""
        self.click(self.back_to_profile_button)

    def search_friend(self, text: str):
        """Enters the specified text into the search input field."""
        self.find(self.search_input).send_keys(text)

    def is_page_loaded(self):
        """Checks if the page is loaded by verifying the presence of the friend tabs."""
        return self.find(self.friend_tabs).is_displayed()

    @allure.step("Navigating to the About Us page from Friends page")
    def go_to_about_us(self):
        """Navigate to the About Us page."""
        from pages.about_us_page import AboutUsPage  # pylint: disable=import-outside-toplevel
        self.header.click_about_us_link()
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("about")
        )
        return AboutUsPage(self.driver)

    @allure.step("Checking if My Friends page is opened")
    def is_page_opened(self) -> bool:
        """Check if the page is opened."""
        return self.is_visible(self.title_locator)
