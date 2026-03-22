"""Step definitions for testing the habit duration slider."""

import time

# pylint: disable=not-callable

from behave import given, then, when

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage
from pages.habit_pages.one_habit_page import OneHabitPage


@given('the user has opened a habit card')
def step_impl_open_habit(context):
    """Open a habit card from the user's space to edit its details."""
    driver = context.browser
    page = MyHabitPage(driver)

    habit_card = page.get_habit_card()
    habit_card.click_edit_habit()


@given('the duration slider is initially set to the default value of "{expected_value}"')
def step_impl_check_default_slider(context, expected_value):
    """Verify that the duration slider starts at the expected default value."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    one_habit_page.move_slider_left(57)
    actual_value = one_habit_page.get_slider_value()
    assert actual_value == int(expected_value), \
        f"Expected default {expected_value}, but got {actual_value}"


@when('the user drags the slider handle to the maximum right position')
def step_impl_drag_max_right(context):
    """Attempt to drag the slider handle far past its maximum right limit."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    one_habit_page.move_slider_right(60)


@then('the text indicator should display the maximum value of "{expected_value}"')
def step_impl_verify_max_value(context, expected_value):
    """Verify that the slider stops exactly at the maximum allowed boundary."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    actual_value = one_habit_page.get_slider_value()
    assert actual_value == int(expected_value), \
        f"Slider crossed max boundary. Expected {expected_value}, got {actual_value}"


@when('the user drags the slider handle to the minimum left position')
def step_impl_drag_min_left(context):
    """Attempt to drag the slider handle far past its minimum left limit."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    one_habit_page.move_slider_left(60)


@then('the text indicator should display the minimum value of "{expected_value}"')
def step_impl_verify_min_value(context, expected_value):
    """Verify that the slider stops exactly at the minimum allowed boundary."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    actual_value = one_habit_page.get_slider_value()
    assert actual_value == int(expected_value), \
        f"Slider crossed min boundary. Expected {expected_value}, got {actual_value}"


@when('the user adjusts the duration slider to "{target_days}" days')
def step_impl_adjust_slider(context, target_days):
    """Dynamically adjust the slider to a specific target day value."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    target = int(target_days)
    current = one_habit_page.get_slider_value()

    difference = target - current
    if difference > 0:
        one_habit_page.move_slider_right(difference)
    elif difference < 0:
        one_habit_page.move_slider_left(abs(difference))

    time.sleep(0.5)  # Даємо UI час оновитися


@then('the habit duration should be successfully updated to "{expected_days}" days')
def step_impl_verify_updated_duration(context, expected_days):
    """Verify that the slider has successfully updated to the chosen duration."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    actual_value = one_habit_page.get_slider_value()
    assert actual_value == int(expected_days), \
        f"Failed to update duration. Expected {expected_days}, got {actual_value}"
