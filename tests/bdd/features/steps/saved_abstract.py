# pylint: disable=not-callable, unused-argument
""" :module:: SavedAbstract
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from pages.abstract_pages.saved_abstract.saved_abstract import SavedAbstract
from pages.common_pages.main_page import MainPage

from data.config import Config

@given("the user is logged in")
def user_logged_in(driver):
    """Log in"""
    main_page = MainPage(driver)

    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given("the Saved page is opened")
def open_saved_page(driver):
    """Opening of Saved page"""
    main_page = MainPage(driver)
    saved_page = main_page.go_to_saved()

    assert saved_page.is_page_opened(), "Saved page is not opened"
    return saved_page



@then("all tabs on the Saved page should be visible")
def verify_tabs_visible(saved_page):
    """Verify tabs is visible"""
    tabs_component = saved_page.get_tabs_component()
    assert tabs_component is not None


@then("the Saved page header should be visible")
def verify_saved_page_header(saved_page):
    """Verify saved """
    assert saved_page.is_page_opened()


@then("the section heading should be displayed")
def verify_section_heading(saved_page):
    """Verify section header"""
    heading = saved_page.get_section_heading()
    assert heading != ""



@when("I go to the Saved Events tab")
def go_to_events_tab(saved_page):
    """Go to Events tab"""
    return saved_page.go_to_tab("Events")


@when("I go to the Saved Places tab")
def go_to_places_tab(saved_page):
    """Go to Places tab"""
    return saved_page.go_to_tab("Places")


@when("I go to the Saved News tab")
def go_to_news_tab(saved_page):
    """Go to News tab"""
    return saved_page.go_to_tab("Eco-news")



@then("the Saved Events tab should be opened")
def verify_events_tab(driver):
    """Verify Events tab is opened"""
    page = SavedAbstract(driver)
    assert page.is_page_opened(), "Saved Events tab is not opened"


@then("the Saved Places tab should be opened")
def verify_places_tab(driver):
    """Verify Places tab is opened"""
    page = SavedAbstract(driver)
    assert page.is_page_opened(), "Saved Places tab is not opened"


@then("the Saved News tab should be opened")
def verify_news_tab(driver):
    """Verify News tab is opened"""
    page = SavedAbstract(driver)
    assert page.is_page_opened(), "Saved News tab is not opened"


@then("the Saved page should be loaded")
def verify_saved_page_loaded(driver):
    """Verify Saved page is loaded"""
    page = SavedAbstract(driver)
    assert page.is_loaded()


@when('I navigate to tab "{tab_name}"')
def go_to_any_tab(saved_page, tab_name):
    """Go to tab by name"""
    return saved_page.go_to_tab(tab_name)
