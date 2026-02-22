import allure


@allure.title("Test for successful habit creation")
def test_successful_habit_creation(driver_delete_habit_after):
    """Check that user is able to create a new habit card by
    filling in all required fields on the Create habit page."""

    create_habit_page = driver_delete_habit_after.create_page
    all_habits_page = driver_delete_habit_after.list_page

    create_habit_page.basic_form.enter_title("Test title")
    create_habit_page.basic_form.choose_tags(["testing"])
    create_habit_page.basic_form.enter_description("Test habit description")

    submit_btn = create_habit_page.basic_form.add_habit_btn
    assert submit_btn.is_enabled(), "Add Habit button should be enabled"

    create_habit_page.basic_form.submit_form()
    habit_cards = all_habits_page.get_all_habit_cards()

    habit_title = habit_cards[0].get_habit_info()["title"]
    assert habit_title == "Test title", "Wrong title"
