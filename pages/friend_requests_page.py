"""Module contains FriendRequestsPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage

class FriendRequestsPage(BasePage):
    """Page Object for Friends -> Requests page (base skeleton)"""

    page_title_locator = (By.XPATH, "//h1[contains(.,'Друзі')]")
    requests_tab_locator = (By.XPATH, "//*[contains(.,'Запити')]")

    def get_title(self):
        """Return page title text."""
        return self.driver.find_element(*self.page_title_locator).text

    def click_requests_tab(self):
        """Click on Requests tab."""
        self.driver.find_element(*self.requests_tab_locator).click()
