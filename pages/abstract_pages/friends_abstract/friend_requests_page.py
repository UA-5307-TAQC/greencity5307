"""Module contains FriendRequestsPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from utils.types import Locators


class FriendRequestsPage(BasePage):
    """Page Object for Friends -> Requests page."""

    page_title_locator: Locators = (By.XPATH, "//h1[contains(., 'Друзі')]")

    requests_tab_locator: Locators = (
        By.XPATH,
        "//a[contains(text(),'Friend requests') or contains(text(),'Запити')]"
    )

    search_input_locator: Locators = (By.CSS_SELECTOR, "input.search")

    friend_name_locator: Locators = (
        By.XPATH, "//p[contains(@class,'friend-name')]")

    my_space_tab_locator: Locators = (
        By.XPATH, "//a[contains(.,'Мій кабінет')]")

    plus_my_friends_click: Locators = (
        By.XPATH, "//a[normalize-space(text()) = '+']")

    def click_my_space_tab(self) -> None:
        """Click My space tab."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.my_space_tab_locator)
        ).click()

    def click_plus_friends(self) -> None:
        """Click '+ friends' link/button."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.plus_my_friends_click)
        ).click()

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

    def is_search_input_visible(self) -> bool:
        """Search input is visible."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input_locator)
        ).is_displayed()

    def search(self, text: str) -> None:
        """Partial search."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input_locator)
        )

        search_input.clear()
        search_input.send_keys(text)

    def get_search_value(self) -> str:
        """Return current value of search input."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input_locator)
        )
        return search_input.get_attribute("value")

    def is_search_value(self, expected: str) -> bool:
        """Verify that input contains entered text."""
        return self.get_search_value() == expected

    def are_matching_results_displayed(self, query: str) -> bool:
        """Verify matching results are shown."""
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.friend_name_locator)
        )
        elements = self.driver.find_elements(*self.friend_name_locator)
        names = [el.text.strip() for el in elements]

        return (
            len(names) > 0 and
            all(query.lower() in name.lower() for name in names)
        )

    def search_input_clear(self) -> None:
        """Clear input."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input_locator)
        )

        search_input.clear()

    def is_search_empty(self) -> bool:
        """Check if search input is empty."""
        search_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.search_input_locator)
        )
        return search_input.get_attribute("value") == ""

    def get_requests_count(self) -> int:
        """Return number of displayed friend requests."""
        elements = self.driver.find_elements(*self.friend_name_locator)
        return len(elements)

    def verify_requests_list_is_restored(self, initial_count: int) -> bool:
        """Request list is restored."""
        try:
            WebDriverWait(self.driver, 10).until(
                lambda d: len(d.find_elements(
                    *self.friend_name_locator)) == initial_count
            )
            return True
        except TimeoutException:
            return False

    def no_results_are_displayed(self) -> bool:
        """Verify no results are shown/empty results state."""
        WebDriverWait(self.driver, 10).until(
            lambda d: len(d.find_elements(*self.friend_name_locator)) == 0
        )
        return True
