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
from fixtures.ui_fixtures import browser, fixture_registry


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


def before_scenario(context, scenario): # pylint: disable=unused-argument
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
        return

    # Provide a default browser fixture for scenarios that don't have an
    # explicit fixture tag. This prevents steps that reference
    # `context.browser` from failing with AttributeError.
    use_fixture(browser, context)
