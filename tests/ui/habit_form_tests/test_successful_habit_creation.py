import allure


@allure.title("Test for successful habit creation")
def test_successful_habit_creation(driver_delete_habit_after):
    """Check that user is able to create a new habit card by
    filling in all required fields on the Create habit page."""

    with allure.step("Go to all habits page"):
        create_habit_page = driver_delete_habit_after.create_page
        all_habits_page = driver_delete_habit_after.all_habits_page

    with allure.step("Enter valid data into required fields"):
        habit_basic_form = create_habit_page.basic_form
        habit_basic_form.enter_title("Test title")
        habit_basic_form.choose_tags(["testing"])
        habit_basic_form.enter_description("Test habit description")

    with allure.step("Check if submit button is enabled and submit the form"):
        submit_btn = habit_basic_form.add_habit_btn
        assert submit_btn.is_enabled(), "Add Habit button should be enabled"
        habit_basic_form.submit_form()

    with allure.step("Find the first habit and check if the title is correct"):
        habit_cards = all_habits_page.get_all_habit_cards()
        habit_title = habit_cards[0].get_habit_info()["title"]
        assert habit_title == "Test title", "Wrong title"
