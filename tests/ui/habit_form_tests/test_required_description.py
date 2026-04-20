import allure

@allure.title("Empty Description Textarea")
@allure.description("Check that user is not able to submit a form on the Create Habit page "
              "after leaving the 'Habit description' textarea empty")
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Liubov Titova")
@allure.testcase("https://github.com/UA-5307-TAQC/greencity5307/issues/27", "TC-003")
def test_description_is_required(create_habit_page_context):
    """Test that 'Habit description' textarea is required."""

    with allure.step("Go to Create Habit page"):
        create_habit_page = create_habit_page_context.create_page
        habit_basic_form = create_habit_page.basic_form

    with allure.step("Click on the description textarea and leave it empty"):
        habit_basic_form.description.wait_and_click()

    with allure.step("Enter valid title and choose a tag"):
        create_habit_page.basic_form.enter_title("Test title")
        create_habit_page.basic_form.choose_tags(["testing"])

    with allure.step("Check if the description validation message is displayed"):
        description_validation = habit_basic_form.get_description_validation()
        assert description_validation.is_displayed()

    with allure.step("Check that submit button isn't enabled after leaving description textarea empty"):
        submit_btn = create_habit_page.basic_form.add_habit_btn
        assert not submit_btn.is_enabled(), \
            "Add Habit button shouldn't be enabled - description textarea is empty"
