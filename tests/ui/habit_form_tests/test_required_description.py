import allure


@allure.title("Test that 'Habit description' textarea is required")
def test_description_is_required(create_habit_page_context):
    """Check that user is not able to submit a form on the Create habit page
    after leaving the "Habit description" textarea empty."""

    create_habit_page = create_habit_page_context.create_page

    create_habit_page.basic_form.enter_title("Test title")
    create_habit_page.basic_form.choose_tags(["testing"])

    submit_btn = create_habit_page.basic_form.add_habit_btn
    assert not submit_btn.is_enabled(), "Add Habit button shouldn't be enabled"
