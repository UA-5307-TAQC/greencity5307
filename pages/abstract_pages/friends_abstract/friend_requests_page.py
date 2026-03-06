"""Module contains FriendRequestsPage page object."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from utils.types import Locators


class FriendRequestsPage(BasePage): # pylint: disable=too-many-public-methods
    """Page Object for Friends -> Requests page (Factory style)."""

    title_locator: Locators = (
        By.XPATH,
        "//h1[contains(., 'Друзі') or contains(., 'Friends')]"
    )

    locators = {
        "my_space_tab": (
            By.XPATH,
            "//a[contains(.,'Мій кабінет') or contains(., 'My Space')]",
        ),  # pylint: disable=duplicate-code
        "plus_friends_btn": (By.XPATH, "//a[contains(.,'+')]"),
        "requests_tab": (
            By.XPATH,
            "//a[contains(.,'Запити') or contains(.,'Friend requests')]",
        ),  # pylint: disable=duplicate-code
        "my_friends_tab": (
            By.XPATH,
            "//a[contains(.,'Мої друзі') or contains(.,'My friends')]",
        ),
        "search_input": (By.CSS_SELECTOR, "input.search")
    }

    friend_name_in_card_locator: Locators = (
        By.XPATH, "//*[contains(@class,'friend-item-wrapper')]//p[contains(@class,'friend-name')]"
    )

    no_results_locator: Locators = (
        By.CSS_SELECTOR,
        "p.noFriends",
    )
    request_card_locator: Locators = (
        By.XPATH, "//*[contains(@class,'friend-item-wrapper')]"
    )
    accept_button_in_card_locator: Locators = (
        By.XPATH, ".//button[contains(@id,'acceptRequest')]"
    )

    # Search in the Requests tab
    def click_my_space_tab(self) -> None:
        """Click My Space tab."""
        self.get_wait().until(
            EC.element_to_be_clickable(self.locators["my_space_tab"])
        ).click()

    def click_plus_friends(self) -> None:
        """Click '+' to open Friends section."""
        self.get_wait().until(
            EC.element_to_be_clickable(self.locators["plus_friends_btn"])
        ).click()

    def click_requests_tab(self) -> None:
        """Open Requests tab."""
        self.get_wait().until(
            EC.element_to_be_clickable(self.locators["requests_tab"])
        ).click()
        self.get_wait().until(EC.url_contains("/friends/requests"))

    def get_title(self) -> str:
        """Return page title text."""
        return self.get_wait().until(
            EC.visibility_of_element_located(self.title_locator)
        ).text

    def is_search_input_visible(self) -> bool:
        """Return True if search input is visible."""
        return self.get_wait().until(
            EC.visibility_of_element_located(self.locators["search_input"])
        ).is_displayed()

    def search(self, text: str) -> None:
        """Type query into search input (clears before typing)."""
        search_input = self.get_wait().until(
            EC.element_to_be_clickable(self.locators["search_input"])
        )
        search_input.clear()
        search_input.send_keys(text)

    def clear_search(self) -> None:
        """Clear search input."""
        search_input = self.get_wait().until(
            EC.element_to_be_clickable(self.locators["search_input"])
        )
        search_input.clear()

    def get_search_value(self) -> str:
        """Return current value of search input."""
        search_input = self.get_wait().until(
            EC.visibility_of_element_located(self.locators["search_input"])
        )
        return (search_input.get_attribute("value") or "").strip()

    def is_search_value(self, expected: str) -> bool:
        """Verify that input contains entered text."""
        return self.get_search_value() == expected

    def is_search_empty(self) -> bool:
        """Check if search input is empty."""
        return self.get_search_value() == ""

    def get_requests_count(self) -> int:
        """Return number of displayed friend requests (by names)."""
        return len(self.driver.find_elements(*self.friend_name_in_card_locator))

    def wait_requests_present(self) -> None:
        """Wait until at least one request is present."""
        self.get_wait().until(
            lambda d: len(d.find_elements(*self.friend_name_in_card_locator)) > 0
        )

    def get_request_usernames(self) -> list[str]:
        """Return list of usernames displayed in requests list."""
        elements = self.driver.find_elements(*self.friend_name_in_card_locator)
        return [el.text.strip() for el in elements if el.text.strip()]

    def are_matching_results_displayed(self, query: str) -> bool:
        """Verify that all shown usernames contain query (case-insensitive)."""
        self.get_wait().until(
            EC.presence_of_all_elements_located(self.friend_name_in_card_locator)
        )
        names = self.get_request_usernames()
        q = query.lower()
        return len(names) > 0 and all(q in name.lower() for name in names)

    def verify_requests_list_is_restored(self, initial_count: int) -> bool:
        """Wait until list count equals initial_count."""
        try:
            self.get_wait(timeout=10).until(
                lambda d: len(
                    d.find_elements(*self.friend_name_in_card_locator)
                ) == initial_count
            )
            return True
        except TimeoutException:
            return False

    def no_results_are_displayed(self) -> bool:
        """Return True if empty-state is shown OR no visible results remain."""
        wait = self.get_wait(timeout=10)

        def predicate(d) -> bool:
            # 1) Empty-state text block (p.noFriends)
            msg = d.find_elements(*self.no_results_locator)
            if msg and msg[0].is_displayed():
                return True

            # 2) Fallback: no visible names in list
            names = d.find_elements(*self.friend_name_in_card_locator)
            return bool(names) and all(not el.is_displayed() for el in names)

        try:
            wait.until(predicate)
            return True
        except TimeoutException:
            return False

    # Accept friend request
    def open_friends_section(self) -> None:
        """Open friends section via + (or later you can add 'See all')."""
        self.click_plus_friends()

    def open_requests_tab(self) -> None:
        """Open 'Requests' tab."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["requests_tab"])).click()
        self.get_wait().until(EC.url_contains("/friends/requests"))

    def open_my_friends_tab(self) -> None:
        """Open 'My Friends' tab."""
        self.get_wait().until(EC.element_to_be_clickable(
            self.locators["my_friends_tab"])).click()
        self.get_wait().until(EC.url_matches(r".*/friends$"))

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

    # Open Requests tab
    def is_requests_tab_opened(self) -> bool:
        """Requests tab considered opened if URL contains /friends/requests."""
        return "/friends/requests" in self.driver.current_url

    def is_empty_state_visible(self) -> bool:
        """True if empty-state message is visible."""
        try:
            return self.get_wait(timeout=10).until(
                EC.visibility_of_element_located(self.no_results_locator)
            ).is_displayed()
        except TimeoutException:
            return False
