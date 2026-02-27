"""Module for testing search functionality in Friend Requests page."""

from selenium.webdriver.remote.webdriver import WebDriver
import pytest
import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.friends_abstract.friend_requests_page import FriendRequestsPage
from pages.common_pages.main_page import MainPage

@allure.title("Search friend requests by partial username")
@allure.feature("Friends")
@allure.story("Friend Requests - Search")
def test_search_requests_by_partial_username(driver: WebDriver):
    """Test Friend Page search."""

    with allure.step("Open main page and sign in"):
        main_page = MainPage(driver)
        sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
        sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    with allure.step("Link to my space page"):
        main_page.header.click_my_space()

    with allure.step("Open Friends page and switch to Requests tab"):
        friend_requests_page = FriendRequestsPage(driver)
        friend_requests_page.click_plus_friends()
        friend_requests_page.click_requests_tab()

    with allure.step("Locate search input"):
        assert friend_requests_page.is_search_input_visible()

    with allure.step("Save initial list size (needed for step 10)"):
        initial_count = friend_requests_page.get_requests_count()
        if initial_count == 0:
            pytest.skip("No friend requests available to validate search filtering/restoring.")

    with allure.step("Enter partial username -> list updated -> verify matching results"):
        first_name = driver.find_elements(*friend_requests_page.friend_name_locator)[0].text.strip()
        query = first_name[:3] if len(first_name) >= 3 else first_name

        friend_requests_page.search(query)
        assert friend_requests_page.is_search_value(query)
        assert friend_requests_page.are_matching_results_displayed(query)

    with allure.step("Clear input -> verify empty -> verify full list restored"):
        friend_requests_page.search_input_clear()
        assert friend_requests_page.is_search_empty()
        assert friend_requests_page.verify_requests_list_is_restored(initial_count)

    with allure.step("Enter non-existing username -> verify no results state"):
        non_existing = "qwerty_no_such_user_12345"
        friend_requests_page.search(non_existing)
        assert friend_requests_page.is_search_value(non_existing)
        assert friend_requests_page.no_results_are_displayed()
