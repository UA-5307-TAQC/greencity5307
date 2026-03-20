# pylint: disable=not-callable, unused-argument
"""
.. module:: common
    :platform: Unix
    :synopsis: """
import behave
from behave import given, when, then, step


@given('the user opens the website')
def opens_website(context):
    """open website"""
    context.browser.get("/news")


@step("the homepage loads successfully")
def homepage_loads(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: And the homepage loads successfully')


@given('the current website language is "{current_language}"')
def current_website_language(context: behave.runner.Context, current_language: str):
    """
    :type context: behave.runner.Context
    :type current_language: str
    """
    # raise NotImplementedError(u'STEP: Given the current website language is "<current_language>"')


@when("the user opens the language switcher")
def pens_language_switcher(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: When the user opens the language switcher')


@step('selects "{new_language}"')
def selects(context: behave.runner.Context, new_language: str):
    """
    :type context: behave.runner.Context
    :type new_language: str
    """
    # raise NotImplementedError(u'STEP: And selects "<new_language>"')


@then("the page reloads")
def page_reloads(context: behave.runner.Context):
    """
    :type context: behave.runner.Context
    """
    # raise NotImplementedError(u'STEP: Then the page reloads')


@step('the navigation menu displays "{menu_text}"')
def step_impl(context: behave.runner.Context, menu_text: str):
    """
    :type context: behave.runner.Context
    :type menu_text: str
    """
    # raise NotImplementedError(u'STEP: And the navigation menu displays "<menu_text>"')
