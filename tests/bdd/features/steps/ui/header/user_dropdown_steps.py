# pylint: disable=not-callable, unused-argument
"""
.. module:: Dropdown menu
    :platform: Unix
    :synopsis: """
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.abstract_pages.my_space_abstract.my_space_abstract_page import MySpaceAbstractPage


#
# @given('the user is successfully logged in')
# def step_user_successfully_logged_in(context):
#     """Get driver from context and make login."""
#     main_page = MainPage(context.browser)
#     sign_in_form = main_page.header.click_sign_in_link()
#     sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()
#
#     main_page.get_wait().until(
#         EC.url_contains("profile"),
#         message=("URL did not change to profile after login. Current URL: "
#                  f"{context.browser.current_url}")
#     )
#

@given('the header is visible')
def step_header_visible(context):
    """Check if header is visible."""
    main_page = MainPage(context.browser)
    assert main_page.header.is_displayed(), "Header is not visible"


# Info about user in header

@then('the user avatar or username is displayed in the top-right corner')
def step_avatar_displayed(context):
    """Check if user avatar or username is displayed in the top-right corner"""
    my_space_page = MySpaceAbstractPage(context.browser)
    assert my_space_page.user_name.is_displayed(), "User name/avatar is not displayed in the header."


@then('the displayed username corresponds to the logged-in account')
def step_username_corresponds(context):
    """Check if displayed username is correct."""
    my_space_page = MySpaceAbstractPage(context.browser)
    actual_name = my_space_page.user_name.text
    assert actual_name == Config.USER_NAME, f"Expected user name '{Config.USER_NAME}', but got '{actual_name}'."


# Open dropdown menu

@when('the user clicks on the username or avatar in the header')
def step_click_avatar(context):
    """Click on the username or avatar in the header."""
    main_page = MainPage(context.browser)
    main_page.header.click_user_menu()


@then('the account dropdown menu expands')
def step_dropdown_expands(context):
    """Check if user dropdown menu expands."""
    main_page = MainPage(context.browser)
    assert main_page.header.user_menu_profile_link.is_displayed(), "Dropdown did not expand!"


@then('the "{option}" option is visible')
def step_option_visible(context, option):
    """Check if option is visible."""
    main_page = MainPage(context.browser)
    if option == "Personal Account":
        assert main_page.header.user_menu_profile_link.is_displayed()
        assert main_page.header.user_menu_profile_link.is_enabled()
    elif option == "Sign out":
        assert main_page.header.user_menu_sign_out_link.is_displayed()
        assert main_page.header.user_menu_sign_out_link.is_enabled()
    else:
        raise ValueError(f"Unknown dropdown option: {option}")


# Redirection to Profile

@given('the account dropdown menu is open')
def step_dropdown_is_open(context):
    """Check if user dropdown menu is open."""
    main_page = MainPage(context.browser)
    main_page.header.click_user_menu()


@when('the user clicks on "Personal Account"')
def step_click_dropdown_profile(context):
    """Click on "Personal Account" option."""
    main_page = MainPage(context.browser)

    context.initial_url = context.browser.current_url
    main_page.header.click_user_menu_profile_link()


@then('the ubs courier page loads successfully')
def step_profile_loads(context):
    """Check if profile settings page loads successfully."""
    main_page = MainPage(context.browser)

    main_page.get_wait().until(
        EC.url_contains("orders"),
        message=f"Did not redirect to the ubs courier page. Current URL: {context.browser.current_url}"
    )
    assert "orders" in context.browser.current_url


# Sign out

@given('the user is on the Profile page')
def step_user_on_profile(context):
    """Check if user is on the Profile page."""
    assert "profile" in context.browser.current_url


@when('selects "Sign out"')
def step_selects_sign_out(context):
    """Select "Sign out" button."""
    main_page = MainPage(context.browser)
    context.initial_url = context.browser.current_url
    main_page.header.click_user_menu_sign_out_link()


@then('the header displays the "Sign in" button instead of the user avatar')
def step_sign_in_button_displayed(context):
    """Check if user has signed out and 'Sign in' button displayed."""
    main_page = MainPage(context.browser)

    main_page.get_wait().until(
        EC.url_contains("greenCity"),
        message=f"Sign out button did not redirect properly. Current URL: {context.browser.current_url}"
    )

    assert main_page.header.sign_in_link.is_displayed(), "Sign in button is not displayed after logout."
