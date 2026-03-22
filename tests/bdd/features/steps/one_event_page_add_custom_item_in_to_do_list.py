"""Step definitions for adding a custom item to a habit's To-Do list."""

import time

# pylint: disable=not-callable

from behave import given, then, when

from data.config import Config
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.common_pages.main_page import MainPage
from pages.habit_pages.one_habit_page import OneHabitPage


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
    time.sleep(1)


@when('the user adds a custom item "{item_name}" to the To-Do list')
def edit_to_do_list(context, item_name):
    """Add a custom item to the habit's To-Do list."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    one_habit_page.press_to_do_list_edit_button()
    time.sleep(1)

    one_habit_page.add_element_into_list(item_name)
    one_habit_page.save_element()


@then('the "{item_name}" item should be displayed in the To-Do list')
def validation_is_displayed(context, item_name):
    """Verify that the custom item is displayed in the To-Do list."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    items = one_habit_page.check_added_element()
    assert item_name in items, f"Text '{item_name}' was not saved in the To-Do list!"
