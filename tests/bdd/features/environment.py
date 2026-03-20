"""Behave environment helpers and fixtures for UI BDD tests.

This module provides the following Behave fixtures and hooks used by the
project's BDD scenarios:

- ``browser``: a fixture that creates a Selenium WebDriver instance (Chrome)
  configured from environment variables and yields it for scenario use.
- ``driver_with_login``: a fixture that uses ``browser`` and performs a
  sign-in flow before returning a logged-in driver.
- ``before_tag``: a hook that allows running Behave fixtures by tag name.
- ``before_scenario``: a hook executed before each scenario that performs
  cleanup of any leftover drivers and ensures a default browser fixture is
  available for steps that expect ``context.browser``.

These helpers centralize browser setup and teardown and make test steps
simpler by guaranteeing the presence of a configured WebDriver on the
``context`` object.
"""
import allure
from behave import use_fixture
from behave.fixture import fixture
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions

from data.config import Config
from pages.common_pages.main_page import MainPage


@fixture
def browser(context):
    """Behave fixture: provide a Selenium Chrome WebDriver.

    The fixture configures ChromeOptions using values from ``Config`` (for
    headless mode, language, window size, etc.), creates a WebDriver, sets
    an implicit wait, navigates to the configured base URL, then yields the
    WebDriver to the scenario. The driver is quit after the scenario ends.

    Args:
        context: Behave context object used to store the created driver on
            ``context.browser``.

    Yields:
        selenium.webdriver.Chrome: the configured Chrome WebDriver instance.
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
    """Behave fixture: provide a WebDriver with a logged-in user.

    This fixture reuses the ``browser`` fixture to obtain a WebDriver,
    performs a sign-in interaction using the application's MainPage and the
    ``Config`` credentials, waits until the post-login page is loaded, and
    yields the authenticated driver for scenario use. The driver is later
    cleaned up by the standard fixture teardown.

    Args:
        context: Behave context object.

    Yields:
        selenium.webdriver.Chrome: an authenticated WebDriver instance.
    """
    driver = use_fixture(browser, context)
    with allure.step(f"Logging in the user with email: {Config.USER_EMAIL}"):
        main_page = MainPage(driver)
        sign_in_form = main_page.header.click_sign_in_link()
        sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()
    yield driver


fixture_registry = {
    "fixture.browser": browser,
    "fixture.driver_with_login": driver_with_login,
}


def before_tag(context, tag):
    """Hook executed before each tag on a scenario.

    If a scenario contains a tag that matches a key in ``fixture_registry``,
    this hook will run the associated fixture and attach its resources to
    the ``context`` (for example, creating ``context.browser``).

    Args:
        context: Behave context object.
        tag: The tag name (string) encountered on the scenario.
    """
    if tag in fixture_registry:
        use_fixture(fixture_registry[tag], context)


def before_scenario(context, scenario):  # pylint: disable=unused-argument
    """Hook executed before each scenario.

    Responsibilities:
    - Safely clean up any leftover WebDriver instances attached to the
      ``context`` from previous scenarios (defensive teardown).
    - Remove stale attributes like ``context.browser`` and
      ``context.driver_with_login`` to avoid leaking drivers between
      scenarios.
    - Ensure a default ``browser`` fixture is created for scenarios that do
      not explicitly request a fixture via tags so that steps can use
      ``context.browser`` without raising AttributeError.

    Args:
        context: Behave context object.
        scenario: The scenario object about to be executed.
    """

    if hasattr(context, "browser"):
        try:
            context.browser.quit()
        except WebDriverException:
            pass
        try:
            delattr(context, "browser")
        except AttributeError:
            pass

    if hasattr(context, "driver_with_login"):
        try:
            context.driver_with_login.quit()
        except WebDriverException:
            pass
        try:
            delattr(context, "driver_with_login")
        except AttributeError:
            pass

    # Provide a default browser fixture for scenarios that don't have an
    # explicit fixture tag. This prevents steps that reference
    # `context.browser` from failing with AttributeError.
    use_fixture(browser, context)
