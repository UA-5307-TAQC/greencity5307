import allure
import pytest

from data.config import Config
from clients.habit_assign_client import HabitAssignClient

CORRECT_HABIT_IDS = [30, 31]
CORRECT_HABIT_ID = 26
INCORRECT_HABIT_ASSIGNED_ID = 0


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

    with allure.step(f"2. Delete assigned habit with assigned id={habit_assign_id} and check that the response code is 200"):
        response = client.delete_habit_assign(habit_assign_id)
        assert response.status_code == 200

    with allure.step("3. Validate that the response body for habit deletion is empty"):
        assert response.text == ""


@allure.title("Test habit deletion without loging and correct assigned id")
def test_habit_deletion_without_loging(assign_habit, clean_habit):
    """Test habit deletion without loging"""
    with allure.step("Create Habit Assign client"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL)

    habits_to_delete = clean_habit.habits_to_delete
    find_assigned_id = clean_habit.find

    with allure.step(f"Pre-condition: Assign habit with id={CORRECT_HABIT_ID}"):
        assign_habit(CORRECT_HABIT_ID)

    with allure.step("1. Find habit assign id for deletion"):
        habit_assign_id = find_assigned_id(CORRECT_HABIT_ID)

    with allure.step(f"2. Send request to delete assigned habit with assigned id={habit_assign_id} and check that the response code is 401"):
        response = client.delete_habit_assign(habit_assign_id)
        assert response.status_code == 401

    with allure.step(f"Post-condition: Find assigned id for habit with id={habit_assign_id} and register for cleanup"):
        habits_to_delete.append(habit_assign_id)


@allure.title("Test habit deletion with incorrect habit assigned id")
def test_habit_deletion_with_incorrect_assigned_id(habit_assign_client):
    "Test habit deletion with incorrect habit assigned id"
    client = habit_assign_client

    with allure.step(f"1. Delete assigned habit with assigned habit id={INCORRECT_HABIT_ASSIGNED_ID} and check that the response code is 404"):
        response = client.delete_habit_assign(INCORRECT_HABIT_ASSIGNED_ID)
        assert response.status_code == 404
