from types import SimpleNamespace

import allure
import pytest

from pages.my_habit_page import MyHabitPage


@pytest.fixture(scope="function")
def create_habit_page_context(driver_with_login):
    """Fixture for navigation to Create Habit page."""
    driver = driver_with_login

    with allure.step("Go to Create Habit page"):
        my_habit_page = MyHabitPage(driver)
        habits_page = my_habit_page.click_add_new_habit_button()

        create_habit_button = habits_page.get_create_habit_button()
        create_habit_page = create_habit_button.click_create_habit_btn()

    return SimpleNamespace(driver=driver, create_page=create_habit_page, all_habits_page=habits_page)


@pytest.fixture(scope="function")
def driver_delete_habit_after(create_habit_page_context):
    """Fixture to delete the created habit after the test."""
    yield create_habit_page_context

    with allure.step("Deleting the created habit"):
        all_habits_page = create_habit_page_context.all_habits_page
        habit_cards = all_habits_page.get_all_habit_cards()
        habit_title = habit_cards[0].get_habit_info()["title"]

        if habit_title == "Test title":
            one_habit_page = habit_cards[0].click_details_btn()
            one_habit_page.click_delete_button()
