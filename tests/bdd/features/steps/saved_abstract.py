# pylint: disable=not-callable, unused-argument
""" :module:: SavedAbstract
    :platform: Unix
    :synopsis: """
from behave import when, then

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract
from pages.common_pages.main_page import MainPage



@when("the user navigates to the Saved page")
def step_go_to_saved(context):
    """Navigation to the Saved page"""
    context.main_page = MainPage(context.browser)
    context.main_page.go_to_saved()


@then("the Saved page should be opened")
def step_verify_saved_page_opened(context):
    """Verification Saved page is opened"""
    context.saved_page = SavedAbstract(context.browser)
    assert context.saved_page.is_page_opened(), "Saved page is not opened"


@when('the user goes to the "{tab_name}" tab')
def step_go_to_tab(context, tab_name):
    """Go to tab"""
    context.saved_page = SavedAbstract(context.browser)
    context.saved_page.go_to_tab(tab_name)


@then('the "{tab_name}" tab should be active')
def step_verify_tab_active(context, tab_name):
    """Verification that tab is active"""
    context.current_tab = SavedAbstract(context.browser)
    assert context.current_tab.is_page_opened(), f"{tab_name} tab is not active"
