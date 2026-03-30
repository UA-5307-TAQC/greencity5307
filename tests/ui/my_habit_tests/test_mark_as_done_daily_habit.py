"""Mark as Done Daily Habit"""

import allure
from pages.habit_pages.one_habit_page import OneHabitPage
from pages.abstract_pages.my_space_abstract.my_habit_page import MyHabitPage

@allure.feature("Daily Habits")
@allure.story("Tracking habit progress")
@allure.title("Verify user can mark a daily habit as done")
@allure.description("This test navigates to a specific habit, clicks 'Mark as done', and verifies that the UI updates the button state and streak text.")
@allure.severity(allure.severity_level.CRITICAL)
def test_mark_as_done_daily_habit(driver_with_login):
    driver = driver_with_login

    with allure.step("Navigate to the specific habit page"):
        page = MyHabitPage(driver)
        habit_card = page.get_habit_card()
        habit_card.click_edit_habit()

    one_habit_page = OneHabitPage(driver)

    one_habit_page.press_mark_as_done_button()

    with allure.step("Verify the habit button changes state to 'done'"):
        assert one_habit_page.is_habit_marked_as_done() == True, \
            "Habit was not marked as done (button class did not change)"

    with allure.step("Verify the progress text indicates the current streak"):
        progress_text = one_habit_page.get_progress_text()
        assert "day in a row" in progress_text, \
            f"Expected success text (streak), but got: '{progress_text}'"
