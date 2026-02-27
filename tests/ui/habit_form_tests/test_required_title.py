import allure

@allure.title("Check that user is not able to submit a form "
              "on the Create Habit page after leaving the 'Title' field empty")
def test_title_is_required(create_habit_page_context):
    """Test that 'Habit title' field is required."""

    with allure.step("Go to Create Habit page"):
        create_habit_page = create_habit_page_context.create_page
        habit_basic_form = create_habit_page.basic_form

    with allure.step("Click on the title field and leave it empty"):
        habit_basic_form.title.wait_and_click()

    with allure.step("Choose a tag and enter valid description"):
        habit_basic_form.choose_tags(["testing"])
        habit_basic_form.enter_description("Test habit description")

    with allure.step("Check if the title validation message is appeared"):
        assert habit_basic_form.title_validation_msg.is_displayed()

    with allure.step("Check that submit button isn't enabled after leaving title field empty"):
        submit_btn = habit_basic_form.add_habit_btn
        assert not submit_btn.is_enabled(), \
        "Add Habit button shouldn't be enabled - title field is empty"
