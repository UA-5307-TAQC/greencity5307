"""Step definitions for adding a custom item to a habit's To-Do list."""

# pylint: disable=not-callable

from behave import then, when

from pages.habit_pages.one_habit_page import OneHabitPage


@when('the user adds a custom item "{item_name}" to the To-Do list')
def edit_to_do_list(context, item_name):
    """Add a custom item to the habit's To-Do list."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    # press_to_do_list_edit_button already waits for the input form to be visible
    one_habit_page.press_to_do_list_edit_button()

    one_habit_page.add_element_into_list(item_name)
    one_habit_page.save_element()


@then('the "{item_name}" item should be displayed in the To-Do list')
def validation_is_displayed(context, item_name):
    """Verify that the custom item is displayed in the To-Do list."""
    driver = context.browser
    one_habit_page = OneHabitPage(driver)

    items = one_habit_page.check_added_element()
    assert item_name in items, f"Text '{item_name}' was not saved in the To-Do list!"
