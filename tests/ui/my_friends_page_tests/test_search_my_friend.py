"""Test for search my friend."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from data.config import Config
from pages.base_page import BasePage
from pages.abstract_pages.friends_abstract.my_friends_page import FriendsPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage


@allure.title("Search friend by full and partial name")
@allure.description(
    "Verify that user can search friends by full and partial name "
    "on Friends page."
)
@allure.severity(allure.severity_level.NORMAL)
def test_search_friend_by_full_and_partial_name(driver: WebDriver):
    """TC-MF-01"""

    base_page = BasePage(driver)

    with allure.step("User signs in"):
        sign_in_component = base_page.header.click_sign_in_link()
        sign_in_component.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("Open Friends page"):
        my_space_page = MySpaceAbstractPage(driver)
        my_space_page.profile_banner.click_view_all_friends()

        friends_page = FriendsPage(driver)

    with allure.step("Verify search field is visible"):
        assert friends_page.search_input.is_displayed()

    with allure.step("Search friend by full name"):
        friends_page.search_friend("test")

    with allure.step("Verify filtered results"):
        friend_cards = friends_page.get_friend_items()
        assert len(friend_cards) >= 1

    with allure.step("Clear search field"):
        friends_page.search_input.clear()

    with allure.step("Search friend by partial name"):
        friends_page.search_friend("te")

    with allure.step("Verify correct friend displayed"):
        friend_cards = friends_page.get_friend_items()
        assert any("test" in card.get_name().lower() for card in friend_cards)

    with allure.step("Open 'Find a friend' tab"):
        friends_page.select_tab("find a friend")

    with allure.step("Verify tab switched"):
        assert friends_page.tab_find_friend.is_displayed()

    with allure.step("Return to My Friends tab"):
        friends_page.select_tab("my friends")
