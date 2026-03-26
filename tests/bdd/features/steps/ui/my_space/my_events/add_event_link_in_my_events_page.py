"""Steps for add_event_link_in_my_events_page bdd test"""
from behave import when, then

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage


@when("the user navigates to the My Events tab")
def step_navigate_to_my_events_tab(context):
    """User navigates to the My Events tab"""
    context.my_habits_page = MyHabitPage(context.browser)
    context.my_events_page = context.my_habits_page.click_my_events_tab()


@when('the user clicks the "Add Event" link')
def step_click_add_event_link(context):
    """User clicks the Add Event link"""
    context.create_event_page = context.my_events_page.navigate_to_add_event_page()


@then("the Create Event page should open")
def step_check_create_event_page_opened(context):
    """Check Create Event page opened"""
    assert context.create_event_page is not None, "Create Event page did not open"


@then('the page header should be "Create event" or "Створити подію"')
def step_check_create_event_header(context):
    """Check header text"""
    header_text = context.create_event_page.page_header.text

    assert header_text in ["Create event", "Створити подію"], (
        f"Unexpected header: {header_text}"
    )
