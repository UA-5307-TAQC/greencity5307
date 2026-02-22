import allure

@allure.title("Test that 'Habit title' field is required")
def test_title_is_required(create_habit_page_context):
    """Check that user is not able to submit a form on the Create habit page
    after leaving the "Title" field empty."""

    create_habit_page = create_habit_page_context.create_page

    create_habit_page.basic_form.choose_tags(["testing"])
    create_habit_page.basic_form.enter_description("Test habit description")

    submit_btn = create_habit_page.basic_form.add_habit_btn
    assert not submit_btn.is_enabled(), "Add Habit button shouldn't be enabled"
