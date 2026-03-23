# pylint: disable=not-callable, unused-argument
"""
.. module:: common
    :platform: Unix
    :synopsis: """
from time import sleep

import behave
from behave import given, when, then, step
from selenium.webdriver.support.ui import WebDriverWait

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
    is_eng = main_page.header.is_language_english()
    if current_language in ("EN") and is_eng:
        return
    main_page.header.switch_language()

    WebDriverWait(context.browser, Config.EXPLICITLY_WAIT).until(
        lambda drv: main_page.header.language_option.text.strip() != "")


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


@given('the user is successfully logged in')
def logged_in(context):
    """Perform user login via the main page header."""
    driver = context.browser

    main_page = MainPage(driver)
    sign_in_modal = main_page.header.click_sign_in_link()
    sign_in_modal.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD)


@given('the user has opened a specific habit')
def step_impl_habit(context):
    """Open a specific habit card for editing."""
    driver = context.browser

    page = MyHabitPage(driver)
    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()
