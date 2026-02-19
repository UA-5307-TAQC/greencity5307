import allure
import pytest

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import Config
from pages.main_page import MainPage
from pages.my_habit_page import MyHabitPage
from pages.all_habits_page import AllHabitPage




@pytest.fixture(scope="function")
def driver_delete_habit_after(driver_with_login):
    """Fixture to delete the created habit after the test."""
    yield driver_with_login

    with allure.step("Deleting the created habit"):
        all_habits_page = AllHabitPage(driver_with_login)
        habit_cards = all_habits_page.get_all_habit_cards()
        habit_title = habit_cards[0].get_habit_info()["title"]

        if habit_title == "Test title":
            one_habit_page = habit_cards[0].click_details_btn()
            one_habit_page.click_delete_button()


@allure.title("Test for successful habit creation")
def test_successful_habit_creation(driver_delete_habit_after):
    """A test for successful habit creation."""

    driver = driver_delete_habit_after

    my_habit_page = MyHabitPage(driver)
    all_habits_page = my_habit_page.click_add_new_habit_button()

    create_habit_button = all_habits_page.get_create_habit_button()
    create_habit_page = create_habit_button.click_create_habit_btn()

    create_habit_page.basic_form.enter_title("Test title")
    create_habit_page.basic_form.choose_tags(["testing"])
    create_habit_page.basic_form.enter_description("Test habit description")

    submit_btn = create_habit_page.basic_form.add_habit_btn
    assert submit_btn.is_enabled(), "Add Habit button should be enabled"

    create_habit_page.basic_form.submit_form()
    habit_cards = all_habits_page.get_all_habit_cards()

    habit_title = habit_cards[0].get_habit_info()["title"]
    assert habit_title == "Test title", "Wrong title"
