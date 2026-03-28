# pylint: disable=not-callable, unused-argument
""" :module:: FriendsAbstract
    :platform: Unix
    :synopsis: """
from behave import when, then

from pages.abstract_pages.friends_abstract.friends_abstract_page import FriendsAbstractPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage


@when("the user navigates to My Space page")
def step_go_to_my_space(context):
    """Navigation to My Space page"""
    context.my_space_page = MySpaceAbstractPage(context.browser)


@when("the user goes to the Friends tab")
def step_go_to_friends_tab(context):
    """navigation to Friends page"""
    context.my_space_page = MySpaceAbstractPage(context.browser)
    context.my_space_page.click_friends_tab()


@then("the Friends page should be opened")
def step_verify_friends_page_opened(context):
    """Verification that friends page is opened"""
    context.friends_page = FriendsAbstractPage(context.browser)
    assert context.friends_page.is_page_loaded(), "Friends page is not opened"


@when('the user goes to "{tab_name}" tab at friends page')
def step_go_to_friends_sub_tab(context, tab_name):
    """Navigation through tabs"""
    context.friends_page = FriendsAbstractPage(context.browser)
    if tab_name == "My Friends":
        context.friends_page.go_to_my_friend_tab()
    elif tab_name == "Find Friends":
        context.friends_page.go_to_find_friend_tab()
    elif tab_name == "Friend Requests":
        context.friends_page.go_to_friend_requests_tab()
    else:
        raise ValueError(f"Unknown Friends tab: {tab_name}")


@then('the "{tab_name}" at friends page tab should be active')
def step_verify_friends_sub_tab_active(context, tab_name):
    """Verification that tab is active"""
    context.friends_page = FriendsAbstractPage(context.browser)
    assert context.current_tab.is_page_loaded(), f"{tab_name} tab is not opened"
