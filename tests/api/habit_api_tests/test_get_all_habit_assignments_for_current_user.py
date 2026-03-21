"""GET /habit/assign/allForCurrentUser"""

import allure
import pytest

from data.config import Config
from clients.habit_assign_client import HabitAssignClient
from schemas.habits.all_habit_assignments_schema import all_habit_assignments_schema


SUPPORTED_LANG_CODE = ["en", "uk"]
INCORRECT_LANG_CODE = "test"
CORRECT_HABIT_ID = 25


@allure.title("Test user can retrieve habit assignments with supported language codes")
@pytest.mark.parametrize("lang", SUPPORTED_LANG_CODE)
def test_get_all_habit_assignments_success(
    assign_habit,
    habit_assign_client,
    validate_json,
    clean_habit,
    lang: str
):
    """Test get habit assignments for current user with supported language codes"""

    with allure.step(f"Pre-condition: Assign habit with id={CORRECT_HABIT_ID}"):
        assign_habit(CORRECT_HABIT_ID)
        habit_assign_id = clean_habit.find(CORRECT_HABIT_ID)
        clean_habit.habits_to_delete.append(habit_assign_id)

    with allure.step("1. Send request to get all habit assignments with supported lang code"):
        response = habit_assign_client.get_all_habit_assignments_for_current_user(lang)
        parsed_data = response.json()

    with allure.step("2. Check that the response code is 200"):
        assert response.status_code == 200

    with allure.step("3. Validate response json schema for all habit assignments"):
        validate_json(all_habit_assignments_schema, parsed_data)



@allure.title("Test user can't retrieve habit assignments with incorrect language code")
def test_get_all_habit_assignments_with_incorrect_lang_code(habit_assign_client):
    """Test get habit assignments for current user with incorrect language code"""

    with allure.step("1. Send request to get all habit assignments with incorrect lang code"):
        response = habit_assign_client.get_all_habit_assignments_for_current_user(INCORRECT_LANG_CODE)

    with allure.step("2. Check that the response code is 400"):
        assert response.status_code == 400


@allure.title("Test user can't retrieve habit assignments without access token")
def test_get_all_habit_assignments_without_login():
    """Test get habit assignments for current user without access token"""

    with allure.step("Pre-condition: Create Habit Assign client without access token"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL)

    with allure.step(f"1. Send request to get all habit assignments without access token"):
        response = client.get_all_habit_assignments_for_current_user(SUPPORTED_LANG_CODE[0])

    with allure.step("2. Check that the response code is 401"):
        assert response.status_code == 401
