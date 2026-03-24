"""Test Friends Abstract: Navigation through tabs."""

import allure

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.abstract_pages.friends_abstract.friends_abstract_page import FriendsAbstractPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.common_pages.main_page import MainPage


@allure.title("Test Validation: friends abstract page navigation through tabs.")
@allure.description("This test verifies that a user "
                    "can successfully navigate through tabs on friends abstract page. ")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "vitalina.kliuieva")
@allure.testcase("TC-101")
def test_friends_abstract_navigation(driver):
    """
        TC-102
        Title: Navigate through tabs
        Author: Vitalina Kliuieva
        Priority: High
    """

    main_page = MainPage(driver)

    sign_in_modal: SignInComponent = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

    my_space_page = MySpaceAbstractPage(driver)
    friends_page: FriendsAbstractPage = my_space_page.click_friends_tab()

    my_friends: FriendsAbstractPage = friends_page.go_to_my_friend_tab()
    assert my_friends.is_page_loaded(), "My Friends page is not opened"

    find_friends: FriendsAbstractPage = friends_page.go_to_find_friend_tab()
    assert find_friends.is_page_loaded(), "Find Friends page is not opened"

    friend_requests: FriendsAbstractPage = friends_page.go_to_friend_requests_tab()
    assert friend_requests.is_page_loaded(), "Friend Requests page is not opened"
