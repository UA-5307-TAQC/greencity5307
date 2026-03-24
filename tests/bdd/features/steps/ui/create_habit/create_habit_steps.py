# pylint: disable=not-callable, unused-argument
"""
.. module:: Header navigation
    :platform: Unix
    :synopsis: """
from behave import given, when, then
from data.config import Config
from pages.common_pages.main_page import MainPage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage


@given('the English version of the site is selected')
def select_english_version(context):
    "Select the English version of the site"
    main_page = MainPage(context.browser)
    context.main_page = main_page

    if not main_page.header.is_language_english():
        main_page.header.other_language_option.wait_and_click()


@given('I am logged in')
def login(context):
    """Login user"""
    sign_in_form = context.main_page.header.click_sign_in_link()
    sign_in_form.sign_in(Config.USER_EMAIL, Config.USER_PASSWORD).wait_page_loaded()


@given('I navigate to the "Create Habit" page')
def got_to_create_habit_page(context):
    """Go to Create Habit page"""
    my_habit_page = MyHabitPage(context.browser)
    all_habits_page = my_habit_page.click_add_new_habit_button()
    create_habit_button = all_habits_page.get_create_habit_button()
    create_habit_page = create_habit_button.click_create_habit_btn()
    context.create_habit_page = create_habit_page


@when('I fill in the "Title" field with "{value}"')
def enter_data_into_title_field(context, value):
    """Enter title"""
    habit_basic_form = context.create_habit_page.basic_form
    habit_basic_form.enter_title(value)


@when('I click on the "{tag_name}" tag chip')
def choose_tag(context, tag_name):
    """Choose tag"""
    habit_basic_form = context.create_habit_page.basic_form
    habit_basic_form.choose_tags([tag_name.lower()])


@when('I fill in the "Description" textarea with "{value}"')
def enter_data_into_description_textarea(context, value):
    """Enter description"""
    habit_basic_form = context.create_habit_page.basic_form
    habit_basic_form.enter_description(value)


@then('the "Add Habit" button should be clickable')
def check_add_habit_button_status(context):
    """Check that [Add Habit] is clickable"""
    habit_basic_form = context.create_habit_page.basic_form
    submit_btn = habit_basic_form.add_habit_btn
    assert submit_btn.is_enabled(), "Add Habit button should be enabled"


@when('I click the "Add Habit" button')
def click_add_habit_button(context):
    """Click [Add Habit] to submit form"""
    habit_basic_form = context.create_habit_page.basic_form
    context.all_habits_page = habit_basic_form.submit_form()


@then('I should be redirected to the "All Habits" page')
def check_all_habits_page_redirection(context):
    """Check that user is redirected to the All Habits page"""
    assert "allhabits" in context.browser.current_url


@then('the first habit in the list should have the title "{expected_title}"')
def check_first_habit_on_all_habits_page(context, expected_title):
    """Check the first habit card"""
    habit_cards = context.all_habits_page.get_all_habit_cards()
    assert habit_cards, "No habit cards found on the 'All Habits' page; expected at least one habit to verify its title"
    actual_title = habit_cards[0].get_habit_info()["title"]
    assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"
    context.first_habit_card = habit_cards[0]


@then('I click on the habit "Test title"')
def open_habit(context):
    """Click on the first habit card"""
    habit_page = context.first_habit_card.click_details_btn()
    context.habit_page = habit_page


@then('I click the "Delete" button')
def delete_habit(context):
    """Click [Delete]"""
    context.habit_page.click_delete_button()


@when('I click on the "Title" field')
def click_on_title_field(context):
    """Click on the 'Title' field and leave it empty"""
    habit_basic_form = context.create_habit_page.basic_form
    habit_basic_form.title.wait_and_click()


@then('I should see an error message for "Title" field')
def check_title_empty_error_msg(context):
    """Check that 'Title' field validation message is displayed"""
    habit_basic_form = context.create_habit_page.basic_form
    title_validation = habit_basic_form.get_title_validation()
    assert title_validation.is_displayed()


@then('the "Add Habit" button shouldn\'t be clickable')
def check_add_habit_button_not_clickable(context):
    """Check that [Add Habit] isn't clickable"""
    habit_basic_form = context.create_habit_page.basic_form
    submit_btn = habit_basic_form.add_habit_btn
    assert not submit_btn.is_enabled(), \
            "Add Habit button shouldn't be enabled when mandatory fields are empty or invalid"


@when('I click on the "Description" textarea')
def click_on_description_field(context):
    """Click on the 'Description' textarea and leave it empty"""
    habit_basic_form = context.create_habit_page.basic_form
    habit_basic_form.description.wait_and_click()


@then('I should see an error message for "Description" textarea')
def check_description_empty_error_msg(context):
    """Check that 'Description' textarea validation message is displayed"""
    habit_basic_form = context.create_habit_page.basic_form
    description_validation = habit_basic_form.get_description_validation()
    assert description_validation.is_displayed()
