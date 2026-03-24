# pylint: disable=not-callable, unused-argument
"""
.. module:: Header navigation
    :platform: Unix
    :synopsis: """
from datetime import datetime
from behave import when, then

from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@when('I click the friends action on my profile banner')
def click_correct_friend_button(context):
    """Click button that redirects user to the friends page"""
    my_habit_page = MyHabitPage(context.browser)
    profile_banner = my_habit_page.profile_banner
    if profile_banner.friends_images_exist():
        profile_banner.click_view_all_friends()
        context.expected_path = "/friends"
    else:
        profile_banner.click_add_friends_btn()
        context.expected_path = "/friends/recommended"


@when('I click the "Edit Profile" button')
def click_edit_profile_button(context):
    """Click edit profile button"""
    my_habit_page = MyHabitPage(context.browser)
    profile_banner = my_habit_page.profile_banner
    profile_banner.click_edit_btn()


@then('I should be redirected to the "Edit Profile" page')
def check_edit_profile_page_rediretcion(context):
    """Check that user is redirected to the Edit Profile page"""
    url = context.browser.current_url
    assert "/edit" in url, f"Expected to be on friends page, but was at: {url}"


@then('I should be redirected to the appropriate friends page')
def check_friends_page_redirection(context):
    """Check that user is redirected to the appropriate friends page"""
    current_url = context.browser.current_url
    assert context.expected_path in current_url, \
        f"Expected path {context.expected_path} not found in {current_url}"


@then('the profile calendar should match the system date:')
def check_current_date(context):
    """Check if the current day on the calendar is correct"""
    my_habit_page = MyHabitPage(context.browser)
    calendar_date = my_habit_page.calendar.get_current_date()

    now = datetime.now()
    system_date_map = {
        "Day": now.strftime("%d"),
        "Month": now.strftime("%m"),
        "Year": now.strftime("%Y")
    }

    for row in context.table:
        part = row['Part']
        actual_value = str(calendar_date[part.lower()])
        expected_value = system_date_map[part]

        assert actual_value == expected_value, \
            f"Expected {part} to be {expected_value}, but got {actual_value}"
