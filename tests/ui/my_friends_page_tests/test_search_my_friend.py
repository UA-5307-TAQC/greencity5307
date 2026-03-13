"""Test for search my friend."""

import allure
from selenium.webdriver.remote.webdriver import WebDriver

from pages.abstract_pages.friends_abstract.my_friends_page import FriendsPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage


@allure.title("Search friend by full and partial name")
@allure.description(
    "Verify that user can search friends by full and partial name "
    "on Friends page."
)
@allure.severity(allure.severity_level.NORMAL)
def test_search_friend_by_full_and_partial_name(driver_with_login: WebDriver):
    """TC-MF-01"""

    with allure.step("Open Friends page"):
        my_space_page = MySpaceAbstractPage(driver_with_login)
        my_space_page.profile_banner.click_view_all_friends()

        friends_page = FriendsPage(driver_with_login)

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
