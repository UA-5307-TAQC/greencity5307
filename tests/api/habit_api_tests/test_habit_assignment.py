"""POST /habit/assign/{habitId}"""

import allure
import pytest

from data.config import Config
from clients.habit_assign_client import HabitAssignClient
from schemas.habits.assigned_habit_schema import assigned_habit_schema

CORRECT_HABIT_IDS = [1, 21]
HABIT_ID = 21
INCORRECT_HABIT_ID = -3
HABIT_ID_TO_ASSIGN = 24


@allure.title("Test habit assignment with login and correct id")
@pytest.mark.parametrize("habit_id", CORRECT_HABIT_IDS)
def test_habit_assignment_with_correct_id(clean_habit, habit_id, validate_json):
    """Test habit assignment with correct id"""
    client = clean_habit.client
    habits_to_delete = clean_habit.habits_to_delete
    find_assigned_id = clean_habit.find

    with allure.step("Pre-condition: Delete habit assignment if it is already assigned"):
        habit_assigned_id = find_assigned_id(habit_id)
        if habit_assigned_id:
            response = client.delete_habit_assign(habit_assigned_id)

    with allure.step(f"1. Assign to the habit with id={habit_id} and check that the response code is 201"):
        response = client.assign_habit_with_default_properties(habit_id)
        assert response.status_code == 201

    with allure.step(f"Post-condition: Find assigned id for habit with id={habit_id} and register for cleanup"):
        habit_assigned_id = find_assigned_id(habit_id)
        habits_to_delete.append(habit_assigned_id)

    with allure.step("Validate response json schema for habit assignment"):
        habit_data = response.json()
        validate_json(assigned_habit_schema, habit_data)


@allure.title("Test habit assignment without login and correct id")
def test_habit_assignment_without_login():
    """Test habit assignment without login"""
    with allure.step("Pre-condition: Create Habit Assign client without access token"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL)

    with allure.step(f"1. Send request to assign the habit and check that the response code is 401"):
        response = client.assign_habit_with_default_properties(HABIT_ID)
        assert response.status_code == 401


@allure.title("Test habit assignment with already assigned habit id")
def test_pre_assigned_habit_assignment(assign_habit, clean_habit):
    """Test habit assignment with already assigned habit id"""
    client = clean_habit.client
    habits_to_delete = clean_habit.habits_to_delete
    find_assigned_id = clean_habit.find

    with allure.step(f"Pre-condition: Assign habit with id={HABIT_ID_TO_ASSIGN}"):
        assign_habit(HABIT_ID_TO_ASSIGN), "Assigned id is None"

    with allure.step(f"1. Assign to the habit  with id={HABIT_ID_TO_ASSIGN} and check that the response code is 400"):
        response = client.assign_habit_with_default_properties(HABIT_ID_TO_ASSIGN)
        assert response.status_code == 400

    with allure.step(f"Post-condition: Find assigned id for habit with id={HABIT_ID_TO_ASSIGN} and register for cleanup"):
        assigned_id = find_assigned_id(HABIT_ID_TO_ASSIGN)
        assert assigned_id is not None, f"There is no assigned id fot habit id = {HABIT_ID_TO_ASSIGN}"
        habits_to_delete.append(assigned_id)


@allure.title("Test habit assignment with login and incorrect id")
def test_habit_assignment_with_incorrect_id(habit_assign_client):
    """Test habit assignment with incorrect id"""
    client = habit_assign_client

    with allure.step(f"1. Assign to the habit id={INCORRECT_HABIT_ID} and check that the response code is 404"):
        response = client.assign_habit_with_default_properties(INCORRECT_HABIT_ID)
        assert response.status_code == 404
