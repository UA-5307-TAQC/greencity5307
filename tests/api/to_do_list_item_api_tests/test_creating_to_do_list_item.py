"""Validation of creating to-do list items"""
import allure
import pytest
from jsonschema import validate

from clients.to_do_list_client import TodoClient
from data.config import Config
from schemas.to_do_lists.to_do_list_schema import todo_item_schema


@allure.title("ToDo list smoke test with schema validation")
@allure.description("Verify that user can retrieve todo list and it matches schema")
@allure.severity(allure.severity_level.NORMAL)
def test_todo_smoke_with_schema(access_token):

    with allure.step("Create TodoClient"):
        client = TodoClient(
            base_url=Config.BASE_API_URL,
            access_token=access_token
        )

    with allure.step("Get habits for current user"):
        response_habits = client.get_habits()
        assert response_habits.status_code == 200

        habits_data = response_habits.json()
        allure.attach(str(habits_data), name="Habits response", attachment_type=allure.attachment_type.JSON)

        habits = habits_data.get("page", [])

        if not habits:
            pytest.skip("No habits found for user")

        habit_id = habits[0]["id"]

    with allure.step(f"Get todo list for habit_id={habit_id}"):
        response = client.get_todo_list(habit_id)

        assert response.status_code in [200, 404]

        if response.status_code == 404:
            pytest.skip("No todo list for this habit")

        data = response.json()
        allure.attach(str(data), name="Todo list response", attachment_type=allure.attachment_type.JSON)

        if not data:
            pytest.skip("Todo list is empty")

    with allure.step("Validate response schema"):
        validate(instance=data, schema=todo_item_schema)
