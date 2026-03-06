from types import SimpleNamespace

import allure
import pytest

from data.config import Config

from clients.habit_assign_client import HabitAssignClient


@pytest.fixture(scope="function")
def find_habit_assign_id(access_token):
    """Fixture that gets user assigned habits data and returns
    a function that finds the habit assign ID"""

    with allure.step("Create Habit Assign client"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL, access_token=access_token)

    def find(habit_id: int) -> int | None:
        response = client.get_all_assigned_habits()
        assert response.status_code == 200, (
            f"Failed to get assigned habits: {response.status_code} - {response.text}"
        )
        data = response.json()
        for habit in data:
            original_id = habit["habit"]["id"]
            if original_id == habit_id:
                return habit["id"]
        return None

    return SimpleNamespace(client=client, find=find)


@allure.title("Test habit assignment with login")
@pytest.mark.parametrize(
    "habit_id, expected_code",
    [
        pytest.param(1, 201, id="successful habit assignment"),
        pytest.param(21, 201, id="successful habit assignment"),
        pytest.param(21, 400, id="assign already assigned habit"),
        pytest.param(-3, 404, id="assign with wrong habit id")
    ]
)
def test_habit_assignment_with_login(access_token, habit_id, expected_code):
    """Test habit assignment by habit ID"""

    with allure.step("Create Habit Assign client"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL, access_token=access_token)

    with allure.step("Assign to the habit and check that the response code is correct"):
        response = client.assign_habit_with_default_properties(habit_id=habit_id)
        assert response.status_code == expected_code


def test_habit_assignment_without_login():
    """Test habit assignment without loging"""

    with allure.step("Create Habit Assign client"):
        client = HabitAssignClient(base_url=Config.BASE_API_URL)

    with allure.step("Assign to the habit and check that the response code is correct"):
        response = client.assign_habit_with_default_properties(habit_id=27)
        assert response.status_code == 401


@pytest.mark.parametrize(
    "habit_id, expected_code, is_habit_id_exist",
    [
        pytest.param(1, 200, True, id="delete assigned habit"),
        pytest.param(21, 200, True, id="delete assigned habit"),
        pytest.param(-3, 404, False, id="delete assigned habit with wrong habit id")
    ]
)
def test_delete_assigned_habit(find_habit_assign_id, habit_id, expected_code, is_habit_id_exist):
    """Test habit deletion by habit assigned ID"""

    client = find_habit_assign_id.client
    find = find_habit_assign_id.find

    if is_habit_id_exist:
        with allure.step("Find habit assign ID for deletion"):
            habit_assign_id = find(habit_id)
    else:
        habit_assign_id = habit_id

    with allure.step("Delete assigned habit and check that the response code is correct"):
        response = client.delete_habit_assign(habit_assign_id=habit_assign_id)
        assert response.status_code == expected_code
