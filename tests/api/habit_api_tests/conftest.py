from types import SimpleNamespace

import allure
import pytest

from data.config import Config
from clients.habit_assign_client import HabitAssignClient


@pytest.fixture(scope="function")
def habit_assign_client(access_token):
    """Fixture that initializes a habit assigned client"""
    with allure.step("Create Habit Assign client"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL, access_token=access_token)
    return client


@pytest.fixture(scope="function")
def habit_manager(habit_assign_client):
    """Fixture that gets user assigned habits data and returns
    a function that finds the habit assign id"""
    client = habit_assign_client

    def _find(habit_id: int) -> int | None:
        with allure.step("Get all assigned habits"):
            response = client.get_all_assigned_habits()
            assert response.status_code == 200, (
                f"Failed to get assigned habits: {response.status_code} - {response.text}"
            )

        with allure.step("Find habit assigned id"):
            data = response.json()
            for habit in data:
                original_id = habit["habit"]["id"]
                if original_id == habit_id:
                    return habit["id"]
        return None

    yield SimpleNamespace(
        client=client,
        find=_find
    )

    with allure.step("Closing Habit Assign session"):
        client.session.close()


@pytest.fixture(scope="function")
def clean_habit(habit_manager):
    """Fixture that deletes an assigned habit by habit assign id"""
    client = habit_manager.client
    habits_to_delete = []

    yield SimpleNamespace(
        client=client,
        habits_to_delete=habits_to_delete,
        find=habit_manager.find
    )

    for habit_assigned_id in habits_to_delete:
        if habit_assigned_id is None:
            continue
        with allure.step(f"Deleting habit {habit_assigned_id}"):
            response = client.delete_habit_assign(habit_assigned_id)
            assert response.status_code == 200


@pytest.fixture(scope="function")
def assign_habit(habit_manager):
    """Fixture that returns a function that assignes a habit by id"""
    client = habit_manager.client
    find = habit_manager.find

    def _assign_habit(habit_id) -> None:
        habit_assign_id = find(habit_id)
        if not habit_assign_id:
            with allure.step(f"Preassign to the habit with id={habit_id}"):
                response = client.assign_habit_with_default_properties(habit_id)
                assert response.status_code == 201

    return _assign_habit
