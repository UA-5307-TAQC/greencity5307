"""DELETE /habit/assign/delete/{habitAssignId}"""

import allure
import pytest

from data.config import Config
from clients.habit_assign_client import HabitAssignClient

CORRECT_HABIT_IDS = [30, 31]
CORRECT_HABIT_ID = 26


@allure.title("Test habit deletion with correct habit assigned id")
@pytest.mark.parametrize("habit_id", CORRECT_HABIT_IDS)
def test_habit_deletion_with_correct_assigned_id(habit_manager, assign_habit, habit_id):
    """Test habit deletion by habit assigned id"""
    client = habit_manager.client
    find_assigned_id = habit_manager.find

    with allure.step(f"Pre-condition: Assign habit with id={habit_id}"):
        assign_habit(habit_id)

    with allure.step("1. Find habit assign id for deletion"):
        habit_assign_id = find_assigned_id(habit_id)
        assert habit_assign_id is not None, f"There is no assigned id fot habit id = {habit_id}"

    with allure.step(f"2. Delete assigned habit with assigned id={habit_assign_id} and check that the response code is 200"):
        response = client.delete_habit_assign(habit_assign_id)
        assert response.status_code == 200

    with allure.step("3. Validate that the response body for habit deletion is empty"):
        assert response.text == ""


@allure.title("Test habit deletion without logging and correct assigned id")
def test_habit_deletion_without_loging(assign_habit, clean_habit):
    """Test habit deletion without logging"""
    with allure.step("Create Habit Assign client"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL)

    habits_to_delete = clean_habit.habits_to_delete
    find_assigned_id = clean_habit.find

    with allure.step(f"Pre-condition: Assign habit with id={CORRECT_HABIT_ID}"):
        assign_habit(CORRECT_HABIT_ID)

    with allure.step("1. Find habit assign id for deletion"):
        habit_assign_id = find_assigned_id(CORRECT_HABIT_ID)
        assert habit_assign_id is not None, f"There is no assigned id fot habit id = {CORRECT_HABIT_ID}"

    with allure.step(f"2. Send request to delete assigned habit with assigned id={habit_assign_id} and check that the response code is 401"):
        response = client.delete_habit_assign(habit_assign_id)
        assert response.status_code == 401

    with allure.step(f"Post-condition: Find assigned id for habit with id={habit_assign_id} and register for cleanup"):
        assert habit_assign_id is not None and isinstance(habit_assign_id, int), (
            f"Expected a valid integer habit_assign_id for cleanup, got {habit_assign_id!r}"
        )
        habits_to_delete.append(habit_assign_id)


@allure.title("Test habit deletion with incorrect data")
@pytest.mark.parametrize("incorrect_data, status_code",
                         [
                            pytest.param(0, 404, id="incorrect habit assigned id"),
                            pytest.param("habitId", 400, id="incorrect data type")
                         ]
)
def test_habit_deletion_with_incorrect_data(habit_assign_client, incorrect_data, status_code):
    """Test habit deletion with incorrect habit assigned id"""
    client = habit_assign_client

    with allure.step(f"1. Delete assigned habit with assigned habit id={incorrect_data} and check that the code is {status_code}"):
        response = client.delete_habit_assign(incorrect_data)
        assert response.status_code == status_code
