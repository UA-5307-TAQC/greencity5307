"""Module contains FriendRequestsPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.types import Locators


class FriendRequestsPage(BasePage):
    """Page Object for Friends -> Requests page."""

    page_title_locator: Locators = (By.XPATH,
                                    "//h1[contains(., 'Друзі') or contains(., 'Friends')]")

    my_space_tab_locator: Locators = (
        By.XPATH, "//a[contains(.,'Мій кабінет') or contains(., 'My Space')]")

    plus_friends_button_locator: Locators = (By.XPATH, "//a[contains(.,'+')]")

    request_card_locator: Locators = (By.XPATH,
                                    "//*[contains(@class,'friend-item-wrapper')]")

    accept_button_in_card_locator: Locators = (By.XPATH, ".//button[contains(@id,'acceptRequest')]")

    friend_name_in_card_locator: Locators = (By.XPATH,
                                        ".//p[contains(@class,'friend-name')]")

    my_friends_tab_locator: Locators = (
        By.XPATH, "//a[contains(.,'Мої друзі') or contains(.,'My friends')]"
    )

    requests_tab_locator: Locators = (
        By.XPATH, "//a[contains(.,'Запити') or contains(.,'Friend requests')]"
    )

    def click_my_space_tab(self) -> None:
        """Click My space tab."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.my_space_tab_locator)
        ).click()

    def click_plus_friends(self) -> None:
        """Click + (open friends section)."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.plus_friends_button_locator)
        ).click()

    def get_title(self) -> str:
        """Return page title text."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.page_title_locator)
        ).text

    def get_request_cards(self) -> list:
        """Return list of friend request cards."""
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(self.request_card_locator)
        )

    def is_any_request_card_visible(self) -> bool:
        """Check if at least one request card is visible."""
        return len(self.driver.find_elements(*self.request_card_locator)) > 0

    def is_accept_button_visible_on_first_card(self) -> bool:
        """Verify Accept button is visible on first request card."""
        first_card = self.get_request_cards()[0]
        btn = first_card.find_element(*self.accept_button_in_card_locator)
        return btn.is_displayed()

    def get_first_request_username(self) -> str:
        """Get username text from first request card."""
        first_card = self.get_request_cards()[0]
        name_el = first_card.find_element(*self.friend_name_in_card_locator)
        return name_el.text.strip()

    def is_user_present_in_my_friends(self, username: str) -> bool:
        """Check that accepted user is present in friends list."""
        locator: Locators = (
            By.XPATH,
            f"//*[contains(@class,'friend-item-wrapper')][.//*[normalize-space()='{username}']]",
        )
        return len(self.driver.find_elements(*locator)) > 0

    def open_my_friends_tab(self) -> None:
        """Open 'My Friends' tab."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.my_friends_tab_locator)
        ).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/friends"))

    def open_requests_tab(self) -> None:
        """Open 'Requests' tab."""
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.requests_tab_locator)
        ).click()
        WebDriverWait(self.driver, 10).until(EC.url_contains("/friends/requests"))

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

        wait = WebDriverWait(self.driver, 15)

        card = wait.until(EC.visibility_of_element_located(card_locator))

        accept_btn_locator: Locators = (By.XPATH, f"{card_xpath}//{accept_btn_xpath[3:]}")
        wait.until(EC.element_to_be_clickable(accept_btn_locator))

        accept_btn = card.find_element(By.XPATH, accept_btn_xpath)
        accept_btn.click()

        wait.until(EC.staleness_of(card))
