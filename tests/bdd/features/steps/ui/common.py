# pylint: disable=not-callable, unused-argument
"""
.. module:: common
    :platform: Unix
    :synopsis: """
from time import sleep

import behave
from behave import given, when, then, step
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import Config
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.common_pages.main_page import MainPage


@given('the user opens the website')
def opens_website(context):
    """open website"""


@step("the homepage loads successfully")
def homepage_loads(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    # wait until the header is present to consider the homepage loaded
    main_page = MainPage(context.browser)
    WebDriverWait(context.browser, Config.EXPLICITLY_WAIT).until(
        lambda drv: main_page.header is not None
    )


@given('the current website language is "{current_language}"')
def current_website_language(context: behave.runner.Context, current_language: str):
    """
    :type context: behave.runner.Context
    :type current_language: str
    """
    # Ensure the site is opened and header component is available
    main_page = MainPage(context.browser)

    # determine if English
    expected_text = ("Нас і сьогодні ми"
                     if current_language == "UA"
                     else "There are of us and today we")

    if main_page.there_are.text != expected_text:
        main_page.header.switch_language()
        main_page.get_wait().until(
            lambda drv: main_page.there_are.text == expected_text,
            message=f"Failed to switch language to {current_language}"
        )


@when("the user opens the language switcher")
def pens_language_switcher(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    main_page = MainPage(context.browser)
    # click the visible language option to open the language dropdown
    main_page.header.language_option.wait_and_click()


@step('selects "{new_language}"')
def selects(context: behave.runner.Context, new_language: str):
    """
    :type context: behave.runner.Context
    :type new_language: str
    """
    # sleep(3)
    main_page = MainPage(context.browser)
    main_page.header.switch_language()


@then("the page reloads")
def page_reloads(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    # Wait a short time for the page to process the language change and reload
    main_page = MainPage(context.browser)
    WebDriverWait(context.browser, Config.EXPLICITLY_WAIT).until(
        lambda drv: main_page.header.language_option.text.strip() != "")


@step('the navigation menu displays "{menu_text}"')
def step_impl(context: behave.runner.Context, menu_text: str):
    """
    :type context: behave.runner.Context
    :type menu_text: str
    """
    sleep(2)
    main_page = MainPage(context.browser)


    actual = main_page.header.new_link.text.strip()
    assert actual == menu_text, f"Expected menu text '{menu_text}', got actual '{actual}'"


@given('the user has opened a specific habit')
def step_impl_habit(context):
    """Open a specific habit card for editing."""
    driver = context.browser

    page = MyHabitPage(driver)
    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()

@given('the user is signed in')
@given('the user is successfully logged in')
@given('User A is logged into the system')
def step_user_successfully_logged_in(context):
    """Get driver from context and make login."""
    main_page = MainPage(context.browser)
    sign_in_form = main_page.header.click_sign_in_link()
    sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()

    main_page.get_wait().until(
        EC.url_contains("profile"),
        message=("URL did not change to profile after login. Current URL: "
                 f"{context.browser.current_url}")
    )
