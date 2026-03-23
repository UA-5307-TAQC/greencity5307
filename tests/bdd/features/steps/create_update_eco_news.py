# pylint: disable=not-callable, unused-argument
""" :module:: CreateUpdateEcoNews
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from pages.news_pages.create_update_eco_news_page import CreateUpdateEcoNewsPage




@given("the CreateUpdateEcoNewsPage is open")
def open_create_eco_news_page(context):
    """Open Create Eco News page and verify it is loaded."""
    context.page = CreateUpdateEcoNewsPage(context.browser)
    assert context.page.is_page_opened()


@then("the page header should be visible")
def verify_page_header(context):
    """Verify that the page header is visible."""
    assert context.page.is_page_opened()


@then("the submit button should be disabled")
def verify_submit_button_disabled(context):
    """Verify that the submit button is initially disabled."""
    assert not context.page.submit_button.is_enabled()


@when("I enter an empty title")
def enter_empty_title(context):
    """Enter an empty title into the form."""
    context.form = context.page.get_form()
    context.form.enter_title("")


@when('I enter title "Save the Planet"')
def enter_valid_title(context):
    """Enter a valid title into the form."""
    context.form = context.page.get_form()
    context.form.enter_title("Save the Planet")


@when("I enter empty tags")
def enter_empty_tags(context):
    """Enter empty tags into the form."""
    context.form.enter_tags("")


@when('I enter tags "Eco, Nature"')
def enter_valid_tags(context):
    """Enter valid tags into the form."""
    context.form.enter_tags("Eco, Nature")


@when('I enter source "Green Blog"')
def enter_source(context):
    """Enter a source value into the form."""
    context.form.enter_source("Green Blog")


@when("I enter content with less than 300 characters")
def enter_short_content(context):
    """Enter invalid short content (less than required length)."""
    context.form.enter_content("Too short content")


@when("I enter content with more than 300 characters")
def enter_valid_content(context):
    """Enter valid content exceeding 300 characters."""
    content = "Eco " * 100  # >300 chars
    context.form.enter_content(content)


@when("I click the submit button")
def click_submit(context):
    """Click the submit button."""
    context.page.click_submit()


@then("the form should not be submitted")
def verify_form_not_submitted(context):
    """Verify that the form submission did not occur."""
    assert context.page.is_page_opened()


@then("the submit button should remain disabled")
def verify_submit_still_disabled(context):
    """Verify that the submit button is still disabled."""
    assert not context.page.submit_button.is_enabled()


@then('the "Create Eco News" page should still be open')
def verify_still_on_page(context):
    """Verify the user remains on the Create Eco News page."""
    assert context.page.is_page_opened()


@then("the form should be submitted")
def verify_form_submitted(context):
    """Verify that the form was successfully submitted."""
    assert "eco-news" in context.browser.current_url


@when("I click the cancel button")
def click_cancel(context):
    """Click the cancel button."""
    context.page.click_cancel()
