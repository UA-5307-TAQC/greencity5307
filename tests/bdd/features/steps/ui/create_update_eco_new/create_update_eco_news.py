# pylint: disable=not-callable, unused-argument
""" :module:: CreateUpdateEcoNews
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from components.common_components.auth_components.signin_modal_component import SignInComponent
from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.news_pages.create_update_eco_news_page import CreateUpdateEcoNewsPage
from pages.news_pages.eco_news_page import EcoNewsPage


@given("the user is on the main page")
def step_open_main_page(context):
    """Open Main page"""
    context.main_page = MainPage(context.browser)


@given("the user is logged in with valid credentials")
def step_login(context):
    """login with valid credentials"""
    context.main_page = MainPage(context.browser)

    sign_in_modal: SignInComponent = context.main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@when("the user navigates to Eco News page")
def step_go_to_eco_news(context):
    """Navigate to Eco News"""
    context.main_page = MainPage(context.browser)
    context.main_page.go_to_eco_news()


@when("the user clicks on create news button")
def step_click_create_news(context):
    """Click create new button"""
    context.news_page = EcoNewsPage(context.browser)
    context.news_page.click_create_button()


@then("the Create Eco News page should be opened")
def step_verify_create_page_opened(context):
    """Create Eco News page is opened"""
    context.create_news_page = CreateUpdateEcoNewsPage(context.browser)
    assert context.create_news_page.is_page_opened(), \
        "Create Eco News page is not opened"


@when("the user fills the eco news form with valid data")
def step_fill_form_valid(context):
    """Fulfilling the form with valid parameters"""
    context.title = "Save the Planet"
    context.tags = ("Events", "News")
    context.source = "https://saving-planet.org/"
    context.content = "Eco content" * 30

    context.form = context.create_news_page.get_form()

    context.form.fill_form(
        title=context.title,
        tags=context.tags,
        source=context.source,
        content=context.content
    )


@then("the form fields should contain entered data")
def step_verify_form_data(context):
    """Verify entered data"""
    assert context.form.get_title() == context.title
    assert context.form.get_source() == context.source
    assert context.form.get_content() == context.content


@when("the user submits the eco news form")
def step_submit_form(context):
    """Submit of form"""
    context.create_news_page.click_submit()


@then("the Create Eco News page should remain opened after submission")
def step_verify_after_submit(context):
    """Verify if Create Eco News page still remains after submission of form"""
    assert context.create_news_page.is_page_opened(), \
        "Create Eco News page is not opened after submit"

@when("the user fills the eco news form with invalid data")
def step_fill_invalid_form(context):
    """Fulfilling the form with not valid data"""
    context.title = ""
    context.tags = ()
    context.source = "invalid-url"
    context.content = "Eco content"

    context.form = context.create_news_page.get_form()

    context.form.fill_form(
        title=context.title,
        tags=context.tags,
        source=context.source,
        content=context.content
    )

@then("the form fields should contain entered invalid data")
def step_verify_invalid_form(context):
    """Verification of invalid data"""
    assert context.form.get_title() == context.title
    assert context.form.get_source() == context.source
    assert context.form.get_content() == context.content

@when("the user tries to submit the eco news form")
def step_try_submit(context):
    """Try to click submit after invalid data enter"""
    context.create_news_page.click_submit()

@then("the submit button should be disabled")
def step_verify_submit_disabled(context):
    """Check of submit button disabled"""
    assert context.create_news_page.is_submit_button_disabled(), \
        "Submit button is enabled for invalid data"
