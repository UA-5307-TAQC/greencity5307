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
from behave import use_fixture
from behave.fixture import fixture
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions

from data.config import Config


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
    use_fixture(browser, context)
