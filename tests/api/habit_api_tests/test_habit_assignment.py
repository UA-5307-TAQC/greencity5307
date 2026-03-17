import allure
import pytest
from jsonschema import validate

from data.config import Config
from clients.habit_assign_client import HabitAssignClient
from schemas.habits.assigned_habit_schema import assigned_habit_schema

CORRECT_HABIT_IDS = [1, 21]
CORRECT_HABIT_ID = 21
INCORRECT_HABIT_ID = -3
PRE_ASSIGNED_HABIT_ID = 24


@allure.title("Test habit assignment with login and correct id")
@pytest.mark.parametrize("habit_id", CORRECT_HABIT_IDS)
def test_habit_assignment_with_correct_id(clean_habit, habit_id):
    """Test habit assignment with correct id"""
    client = clean_habit.client
    habits_to_delete = clean_habit.habits_to_delete
    find_assigned_id = clean_habit.find

    with allure.step(f"1. Assign to the habit with id={habit_id} and check that the response code is 201"):
        response = client.assign_habit_with_default_properties(habit_id)
        assert response.status_code == 201

    with allure.step(f"Post-condition: Find assigned id for habit with id={habit_id} and register for cleanup"):
        assigned_id = find_assigned_id(habit_id)
        assert assigned_id is not None
        habits_to_delete.append(assigned_id)

    with allure.step("Validate response json schema for habit assignment"):
        habit_data = response.json()
        validate(instance=habit_data, schema=assigned_habit_schema)


@allure.title("Test habit assignment without login and correct id")
def test_habit_assignment_without_login():
    """Test habit assignment without login"""
    with allure.step("Pre-condition: Create Habit Assign client without access token"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL)

    with allure.step(f"1. Send request to assign the habit and check that the response code is 401"):
        response = client.assign_habit_with_default_properties(CORRECT_HABIT_ID)
        assert response.status_code == 401



@allure.title("Test habit assignment with already assigned habit id")
def test_pre_assigned_habit_assignment(assign_habit, clean_habit):
    """Test habit assignment with already assigned habit id"""
    client = clean_habit.client
    habits_to_delete = clean_habit.habits_to_delete
    find_assigned_id = clean_habit.find

    with allure.step(f"Pre-condition: Assign habit with id={PRE_ASSIGNED_HABIT_ID}"):
        assign_habit(PRE_ASSIGNED_HABIT_ID)

    with allure.step(f"1. Assign to the habit  with id={PRE_ASSIGNED_HABIT_ID} and check that the response code is 400"):
        response = client.assign_habit_with_default_properties(PRE_ASSIGNED_HABIT_ID)
        assert response.status_code == 400

    with allure.step(f"Post-condition: Find assigned id for habit with id={PRE_ASSIGNED_HABIT_ID} and register for cleanup"):
        assigned_id = find_assigned_id(PRE_ASSIGNED_HABIT_ID)
        assert assigned_id is not None
        habits_to_delete.append(assigned_id)



@allure.title("Test habit assignment with login and incorrect id")
def test_habit_assignment_with_incorrect_id(habit_assign_client):
    """Test habit assignment with incorrect id"""
    client = habit_assign_client

    with allure.step(f"1. Assign to the habit id={INCORRECT_HABIT_ID} and check that the response code is 404"):
        response = client.assign_habit_with_default_properties(INCORRECT_HABIT_ID)
        assert response.status_code == 404
