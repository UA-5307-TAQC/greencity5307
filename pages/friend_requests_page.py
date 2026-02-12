"""Module contains FriendRequestsPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.types import Locators


class FriendRequestsPage(BasePage):
    """Page Object for Friends -> Requests page."""

    page_title_locator: Locators = (By.XPATH, "//h1[contains(., 'Друзі')]")

    requests_tab_locator: Locators = (
        By.XPATH,
        "//a[contains(@href, 'friend-requests') and contains(., 'Запити')]",
    )

    def get_title(self) -> str:
        """Return page title text."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.page_title_locator)
        ).text

    def click_requests_tab(self) -> None:
        """Click on Requests tab."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.requests_tab_locator)
        ).click()
