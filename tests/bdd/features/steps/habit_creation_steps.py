# pylint: disable=not-callable, unused-argument
"""
.. module:: common
    :platform: Unix
    :synopsis: """
import allure
from behave import when, then


@when('I fill in the "{field_name}" field with "{value}"')
def enter_data_into_title_field(context, field_name, value):
    create_habit_page = context.habit_data.create_page
    habit_basic_form = create_habit_page.basic_form
    with allure.step(f"Enter {value} into {field_name}"):
        if field_name == "Title":
            habit_basic_form.enter_title(value)


@when('I click on the "{tag_name}" tag chip')
def choose_tag(context, tag_name):
    create_habit_page = context.habit_data.create_page
    habit_basic_form = create_habit_page.basic_form
    with allure.step(f"Choose tag: {tag_name}"):
        habit_basic_form.choose_tags([tag_name.lower()])


@when('I fill in the "{textarea_name}" textarea with "{value}"')
def enter_data_into_description_textarea(context, textarea_name, value):
    create_habit_page = context.habit_data.create_page
    habit_basic_form = create_habit_page.basic_form
    with allure.step(f"Enter {value} into {textarea_name}"):
        if textarea_name == "Description":
            habit_basic_form.enter_description(value)


@then('the "Add Habit" button should be clickable')
def check_add_habit_button_status(context):
    create_habit_page = context.habit_data.create_page
    submit_btn = create_habit_page.basic_form.add_habit_btn
    with allure.step("Check if submit button is enabled"):
        assert submit_btn.is_enabled(), "Add Habit button should be enabled"


@when('I click the "Add Habit" button')
def click_add_habit_button(context):
    create_habit_page = context.habit_data.create_page
    habit_basic_form = create_habit_page.basic_form
    with allure.step("Submit the form"):
        context.habit_data.all_habits_page = habit_basic_form.submit_form()


@then('I should be redirected to the "All Habits" page')
def check_all_habits_page_redirection(context):
    with allure.step("Verify redirection to All Habits page"):
        assert "allhabits" in context.habit_data.driver.current_url


@then('the first habit in the list should have the title "{expected_title}"')
def check_first_habit_on_all_habits_page(context, expected_title):
    with allure.step("Find the first habit and check the title"):
        all_habits_page = context.habit_data.all_habits_page
        habit_cards = all_habits_page.get_all_habit_cards()

        actual_title = habit_cards[0].get_habit_info()["title"]
        assert actual_title == expected_title, f"Expected '{expected_title}', but got '{actual_title}'"


@then('I click on the habit "Test title"')
def open_habit(context):
    all_habits_page = context.habit_data.all_habits_page
    habit_cards = all_habits_page.get_all_habit_cards()
    habit_title = habit_cards[0].get_habit_info()["title"]

    if habit_title == "Test title":
        context.habit_data.first_habit_page = habit_cards[0].click_details_btn()


@then('I click the "Delete" button')
def delete_habit(context):
    with allure.step("Deleting the created habit"):
        context.habit_data.first_habit_page.click_delete_button()


@when('I click on the "{field_name}" field')
def click_on_title_field(context, field_name):
    with allure.step(f"Click on the {field_name} field and leave it empty"):
        create_habit_page = context.habit_data.create_page
        create_habit_page.basic_form.title.wait_and_click()


@then('I should see an error message for "{field_name}" field')
def check_title_empty_error_msg(context, field_name):
    create_habit_page = context.habit_data.create_page
    with allure.step(f"Check that the {field_name} validation message is displayed"):
        title_validation = create_habit_page.basic_form.get_title_validation()
        assert title_validation.is_displayed()


@then('the "Add Habit" button shouldn\'t be clickable')
def check_add_habit_button_not_clickable(context):
    create_habit_page = context.habit_data.create_page
    with allure.step("Check that submit button isn't enabled after leaving title field empty"):
        submit_btn = create_habit_page.basic_form.add_habit_btn
        assert not submit_btn.is_enabled(), \
               "Add Habit button shouldn't be enabled - title field is empty"


@when('I click on the "{textarea_name}" textarea')
def click_on_description_field(context, textarea_name):
    with allure.step(f"Click on the {textarea_name} textarea and leave it empty"):
        create_habit_page = context.habit_data.create_page
        create_habit_page.basic_form.description.wait_and_click()


@then('I should see an error message for "{textarea_name}" textarea')
def check_description_empty_error_msg(context, textarea_name):
    create_habit_page = context.habit_data.create_page
    with allure.step(f"Check that the {textarea_name} validation message is displayed"):
        description_validation = create_habit_page.basic_form.get_description_validation()
        assert description_validation.is_displayed()
