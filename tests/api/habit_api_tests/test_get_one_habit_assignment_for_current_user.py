"""GET /habit/assign/{habitAssignId}"""

import allure
import pytest

from data.config import Config
from clients.habit_assign_client import HabitAssignClient
from schemas.habits.habit_assignment_schema import habit_assignment_schema


SUPPORTED_LANG_CODE = ["en", "uk"]
INCORRECT_LANG_CODE = "test"
CORRECT_HABIT_ID = 9

@allure.title("Test user can retrieve habit assignment by correct assigned id "
              "and with supported language codes")
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

    with allure.step("3. Validate response json schema for habit assignment with assigned id={}"):
        validate_json(habit_assignment_schema, parsed_data)
