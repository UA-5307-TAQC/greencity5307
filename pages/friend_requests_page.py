"""Module contains FriendRequestsPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.types import Locators


class FriendRequestsPage(BasePage):
    """Page Object for Friends -> Requests page (Factory style)."""

    title_locator: Locators = (
        By.XPATH, "//h1[contains(., 'Друзі') or contains(., 'Friends')]"
    )

    locators = {
        **BasePage.locators,
        "my_space_tab": (
            By.XPATH,
            "//a[contains(.,'Мій кабінет') or contains(., 'My Space')]",
        ),
        "plus_friends_btn": (By.XPATH, "//a[contains(.,'+')]"),
        "requests_tab": (
            By.XPATH,
            "//a[contains(.,'Запити') or contains(.,'Friend requests')]",
        ),
        "my_friends_tab": (
            By.XPATH,
            "//a[contains(.,'Мої друзі') or contains(.,'My friends')]",
        ),
    }

    request_card_locator: Locators = (
        By.XPATH, "//*[contains(@class,'friend-item-wrapper')]"
    )
    accept_button_in_card_locator: Locators = (
        By.XPATH, ".//button[contains(@id,'acceptRequest')]"
    )
    friend_name_in_card_locator: Locators = (
        By.XPATH, ".//p[contains(@class,'friend-name')]"
    )

    def click_my_space_tab(self) -> None:
        """Click My Space tab."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["my_space_tab"])).click()

    def click_plus_friends(self) -> None:
        """Click + (open friends section)."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["plus_friends_btn"])).click()

    def open_friends_section(self) -> None:
        """Open friends section via + (or later you can add 'See all')."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["plus_friends_btn"])).click()

    def open_requests_tab(self) -> None:
        """Open 'Requests' tab."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["requests_tab"])).click()
        self.get_wait().until(EC.url_contains("/friends/requests"))

    def open_my_friends_tab(self) -> None:
        """Open 'My Friends' tab."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["my_friends_tab"])).click()
        self.get_wait().until(EC.url_contains("/friends"))

    def get_request_cards(self) -> list:
        """Return list of friend request cards."""
        return self.get_wait().until(
            EC.visibility_of_any_elements_located(
                self.request_card_locator
            )
        )

    def is_accept_button_visible_on_first_card(self) -> bool:
        """Verify Accept button is visible on first request card."""
        first_card = self.get_request_cards()[0]
        return first_card.find_element(*self.accept_button_in_card_locator).is_displayed()

    def get_first_request_username(self) -> str:
        """Get username text from first request card."""
        first_card = self.get_request_cards()[0]
        return first_card.find_element(*self.friend_name_in_card_locator).text.strip()

    def accept_request_for_user(self, username: str) -> None:
        """Accept friend request for given username."""
        card_xpath = (
            "//*[contains(@class,'friend-item-wrapper')]"
            "[.//p[contains(@class,'friend-name') "
            f"and normalize-space()='{username}']]"
        )
        card_locator: Locators = (By.XPATH, card_xpath)

        accept_btn_xpath = (
            ".//button[contains(.,'Прийняти') "
            "or contains(.,'Accept') "
            "or contains(@id,'acceptRequest')]"
        )

        wait = self.get_wait(timeout=15)

        card = wait.until(EC.visibility_of_element_located(card_locator))
        accept_btn = card.find_element(By.XPATH, accept_btn_xpath)
        wait.until(lambda d: accept_btn.is_enabled())
        accept_btn.click()

        wait.until(EC.staleness_of(card))

    def is_user_present_in_my_friends(self, username: str) -> bool:
        """Check that accepted user is present in friends list."""
        locator: Locators = (
            By.XPATH,
            "//*[contains(@class,'friend-item-wrapper')]"
            f"[.//*[normalize-space()='{username}']]",
        )
        return len(self.driver.find_elements(*locator)) > 0
