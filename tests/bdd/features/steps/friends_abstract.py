# pylint: disable=not-callable, unused-argument
""" :module:: FriendsAbstract
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from data.config import Config
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage
from pages.common_pages.main_page import MainPage


@given("the user is logged in")
def user_logged_in(context):
    """Log in the user using valid credentials."""
    main_page = MainPage(context.browser)
    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given("the Friends page is opened")
def open_friends_page(context):
    """Open the Friends page from My Space and verify it is loaded."""
    my_space_page = MySpaceAbstractPage(context.browser)
    context.friends_page = my_space_page.click_friends_tab()

    assert context.friends_page.is_page_loaded()


@when('I click the "My Friends" button')
def click_my_friends_tab(context):
    """Navigate to the 'My Friends' tab."""
    context.friends_page.go_to_my_friend_tab()


@when('I click the "Friend Request" button')
def click_friend_requests_tab(context):
    """Navigate to the 'Friend Requests' tab."""
    context.friends_page.go_to_friend_requests_tab()


@when('I click the "Find a Friend" button')
def click_find_friend_tab(context):
    """Navigate to the 'Find a Friend' tab."""
    context.friends_page.go_to_find_friend_tab()


@then("the My Friends tab should be opened")
def verify_my_friends_tab(context):
    """Verify that the 'My Friends' tab is opened."""
    assert context.friends_page.is_page_loaded(), "My Friends tab is not opened"


@then("the Friend Requests tab should be opened")
def verify_friend_requests_tab(context):
    """Verify that the 'Friend Requests' tab is opened."""
    assert context.friends_page.is_page_loaded(), "Friend Requests tab is not opened"


@then("the Find a Friend tab should be opened")
def verify_find_friend_tab(context):
    """Verify that the 'Find a Friend' tab is opened."""
    assert context.friends_page.is_page_loaded(), "Find a Friend tab is not opened"


@when("I search for a friend with name {name}")
def search_friend(context, name):
    """Search for a friend by name."""
    context.friends_page.search_friend(name)


@when("I go back to profile page")
def go_back_to_profile(context):
    """Navigate back to the profile page."""
    context.friends_page.go_back_to_profile()
