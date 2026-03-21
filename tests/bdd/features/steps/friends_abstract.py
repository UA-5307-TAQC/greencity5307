# pylint: disable=not-callable, unused-argument
""" :module:: FriendsAbstract
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from data.config import Config
from pages.abstract_pages.friends_abstract.friends_abstract_page import FriendsAbstractPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.common_pages.main_page import MainPage


@given("the user is logged in")
def user_logged_in(driver):
    """User log in"""
    main_page = MainPage(driver)
    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given("the Friends page is opened")
def open_friends_page(driver):
    """Open Friends page"""
    my_space_page = MySpaceAbstractPage(driver)
    friends_page = my_space_page.click_friends_tab()

    assert friends_page.is_page_loaded()
    return friends_page


@when('I click the "My Friends" button')
def click_my_friends_tab():
    """Click my friends button"""
    return open_friends_page.go_to_my_friend_tab()


@when('I click the "Friend Request" button')
def click_friend_requests_tab():
    """Click friends request tab"""
    return open_friends_page.go_to_friend_requests_tab()


@when('I click the "Find a Friend" button')
def click_find_friend_tab():
    """Click find friend tab"""
    return open_friends_page.go_to_find_friend_tab()



@then("the My Friends tab should be opened")
def verify_my_friends_tab(driver):
    """Verify My friends tab is opened"""
    page = FriendsAbstractPage(driver)
    assert page.is_page_loaded(), "My Friends tab is not opened"


@then("the Friend Requests tab should be opened")
def verify_friend_requests_tab(driver):
    """Verify friends requests tab is opened"""
    page = FriendsAbstractPage(driver)
    assert page.is_page_loaded(), "Friend Requests tab is not opened"


@then("the Find a Friend tab should be opened")
def verify_find_friend_tab(driver):
    """Verify find friends tab is opened"""
    page = FriendsAbstractPage(driver)
    assert page.is_page_loaded(), "Find a Friend tab is not opened"


@when("I search for a friend with name {name}")
def search_friend(driver, name):
    """Search friend by name"""
    page = FriendsAbstractPage(driver)
    page.search_friend(name)


@when("I go back to profile page")
def go_back_to_profile(driver):
    """Go back to profile button click"""
    page = FriendsAbstractPage(driver)
    page.go_back_to_profile()
