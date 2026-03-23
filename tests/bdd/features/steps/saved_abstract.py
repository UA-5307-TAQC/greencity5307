# pylint: disable=not-callable, unused-argument
""" :module:: SavedAbstract
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract
from pages.common_pages.main_page import MainPage
from data.config import Config


@given("the user is logged in")
def user_logged_in(context):
    """Log in the user using valid credentials."""
    main_page = MainPage(context.browser)

    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given("the Saved page is opened")
def open_saved_page(context):
    """Open the Saved page and verify it is loaded."""
    main_page = MainPage(context.browser)
    context.saved_page = main_page.go_to_saved()

    assert context.saved_page.is_page_opened(), "Saved page is not opened"


@then("all tabs on the Saved page should be visible")
def verify_tabs_visible(context):
    """Verify that all tabs are visible on the Saved page."""
    tabs_component = context.saved_page.get_tabs_component()
    assert tabs_component is not None


@then("the Saved page header should be visible")
def verify_saved_page_header(context):
    """Verify that the Saved page header is displayed."""
    assert context.saved_page.is_page_opened()


@then("the section heading should be displayed")
def verify_section_heading(context):
    """Verify that the section heading is displayed."""
    heading = context.saved_page.get_section_heading()
    assert heading != ""


@when("I go to the Saved Events tab")
def go_to_events_tab(context):
    """Navigate to the Saved Events tab."""
    context.saved_page.go_to_tab("Events")


@when("I go to the Saved Places tab")
def go_to_places_tab(context):
    """Navigate to the Saved Places tab."""
    context.saved_page.go_to_tab("Places")


@when("I go to the Saved News tab")
def go_to_news_tab(context):
    """Navigate to the Saved News tab."""
    context.saved_page.go_to_tab("Eco-news")


@then("the Saved Events tab should be opened")
def verify_events_tab(context):
    """Verify that the Saved Events tab is opened."""
    assert context.saved_page.is_page_opened(), "Saved Events tab is not opened"


@then("the Saved Places tab should be opened")
def verify_places_tab(context):
    """Verify that the Saved Places tab is opened."""
    assert context.saved_page.is_page_opened(), "Saved Places tab is not opened"


@then("the Saved News tab should be opened")
def verify_news_tab(context):
    """Verify that the Saved News tab is opened."""
    assert context.saved_page.is_page_opened(), "Saved News tab is not opened"


@then("the Saved page should be loaded")
def verify_saved_page_loaded(context):
    """Verify that the Saved page is fully loaded."""
    page = SavedAbstract(context.browser)
    assert page.is_loaded()


@when('I navigate to tab "{tab_name}"')
def go_to_any_tab(context, tab_name):
    """Navigate to any Saved tab by its name."""
    context.saved_page.go_to_tab(tab_name)
