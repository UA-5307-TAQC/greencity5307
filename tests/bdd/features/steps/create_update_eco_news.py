# pylint: disable=not-callable, unused-argument
""" :module:: CreateUpdateEcoNews
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.news_pages.create_update_eco_news_page import CreateUpdateEcoNewsPage

@given("the user is logged in")
def user_logged_in(driver):
    """User log in given"""
    main_page = MainPage(driver)
    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)

@given("the CreateUpdateEcoNewsPage is open")
def open_create_eco_news_page(driver):
    """Verification of opened create eco news page"""
    page = CreateUpdateEcoNewsPage(driver)
    assert page.is_page_opened()
    return page


@then("the page header should be visible")
def verify_page_header():
    """Verify page header"""
    assert open_create_eco_news_page.is_page_opened()


@then("the submit button should be disabled")
def verify_submit_button_disabled():
    """Verification of submit button disabled"""
    assert not open_create_eco_news_page.submit_button.is_enabled()



@when("I enter an empty title")
def enter_empty_title():
    """Enter empty title"""
    form = open_create_eco_news_page.get_form()
    form.enter_title("")


@when('I enter title "Save the Planet"')
def enter_valid_title():
    """Enter valid title"""
    form = open_create_eco_news_page.get_form()
    form.enter_title("Save the Planet")


@when("I enter empty tags")
def enter_empty_tags():
    """Enter empty tags"""
    form = open_create_eco_news_page.get_form()
    form.enter_tags("")


@when('I enter tags "Eco, Nature"')
def enter_valid_tags():
    """Enter valid tags"""
    form = open_create_eco_news_page.get_form()
    form.enter_tags("Eco, Nature")


@when('I enter source "Green Blog"')
def enter_source():
    """Enter invalid source"""
    form = open_create_eco_news_page.get_form()
    form.enter_source("Green Blog")


@when("I enter content with less than 300 characters")
def enter_short_content():
    """Enter invalid content"""
    form = open_create_eco_news_page.get_form()
    form.enter_content("Too short content")


@when("I enter content with more than 300 characters")
def enter_valid_content():
    """Enter valid content"""
    form = open_create_eco_news_page.get_form()
    content = "Eco " * 100  # >300 chars
    form.enter_content(content)


@when("I click the submit button")
def click_submit():
    """Click submit button"""
    open_create_eco_news_page.click_submit()



@then("the form should not be submitted")
def verify_form_not_submitted():
    """Verify form is not submitted"""
    assert open_create_eco_news_page.is_page_opened()


@then("the submit button should remain disabled")
def verify_submit_still_disabled():
    """Verify submit button is disabled"""
    assert not open_create_eco_news_page.submit_button.is_enabled()


@then('the "Create Eco News" page should still be open')
def verify_still_on_page():
    """Verify page is still opened"""
    assert open_create_eco_news_page.is_page_opened()


@then("the form should be submitted")
def verify_form_submitted(driver):
    """Verify form is submitted"""
    # depends on real behavior (URL change / redirect)
    assert "eco-news" in driver.current_url


@when("I click the cancel button")
def click_cancel():
    """Click cancel button"""
    open_create_eco_news_page.click_cancel()
