"""This module defines fixtures and hooks for setting up
and tearing down the test environment for BDD tests using Behave."""
import allure
from behave import use_fixture
from behave.fixture import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from data.config import Config
from pages.common_pages.main_page import MainPage


@fixture
def browser(context):
    """
    Parametrized pytest fixture that returns a Selenium WebDriver for Chrome and Firefox.
    - Param values: "chrome" or "firefox"
    - Set `HEADLESS` env var to `1` or `true` to enable headless mode.
    """
    opts = ChromeOptions()
    if Config.HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument(f"--lang={Config.BROWSER_LANG}")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-gpu")
    opts.add_argument("--window-size=1920,1080")
    context.browser = webdriver.Chrome(options=opts)
    context.browser.implicitly_wait(Config.IMPLICITLY_WAIT)
    context.browser.get(Config.BASE_UI_URL)

    yield context.browser

    context.browser.quit()


@fixture
def driver_with_login(context):
    """Fixture that logs in the user before yielding the WebDriver."""
    driver = use_fixture(browser, context)
    with allure.step(f"Logging in the user with email: {Config.USER_EMAIL}"):
        main_page = MainPage(driver)
        sign_in_form = main_page.header.click_sign_in_link()
        sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()
    yield driver


fixture_registry = {"fixture.browser": browser, "fixture.driver_with_login": driver_with_login, }


def before_tags(context, tags):
    """Before each scenario, check if it has tags that match our fixtures and set them up."""
    if tags in fixture_registry:
        use_fixture(fixture_registry[tags], context)


def before_scenario(context, scenario): #  pylint: disable=unused-argument
    """Before each scenario, check if it has tags that match our fixtures and set them up."""
    if hasattr(context, "browser"):
        context.browser.quit()
    if hasattr(context, "driver_with_login"):
        context.driver_with_login.quit()
