"""Validation of creating to-do list items"""
import allure
import pytest
from jsonschema import validate

from clients.to_do_list_client import TodoClient
from clients.habit_assign_client import HabitAssignClient
from data.config import Config
from schemas.to_do_lists.to_do_list_schema import (todo_item_schema, todo_create_request_schema)

# @pytest.mark.parametrize(
#     "habit_id, body, status_code",
#     [
#         (1, [{"id": 2}], 201),
#         (99999, [{"id": 1}], 400),
#     ]
# )

def test_todo_client_methods_smoke(access_token):

    client = TodoClient(
        base_url=Config.BASE_API_URL,
        access_token=access_token
    )

    response_habits = client.get_habits()
    assert response_habits.status_code == 200

    habits_data = response_habits.json()
    habits = habits_data.get("page", [])

    if not habits:
        pytest.skip("No habits found")

    habit_id = habits[0]["id"]

    # ===================== 2. CREATE TODO =====================
    todo_body = [{"title": "Test Item", "description": "Smoke test"}]
    response_create = client.create_todo_items(habit_id=habit_id, body=todo_body)
    assert response_create.status_code == 201  # створення успішне

    # ===================== 3. GET TODO LIST =====================
    response_todo = client.get_todo_list(habit_id=habit_id)
    assert response_todo.status_code == 200

    todo_items = response_todo.json()
    assert len(todo_items) > 0, "No todo items available"

    item_id = todo_items[0]["id"]

    # ===================== 4. UPDATE STATUS =====================
    response_update = client.update_item_status(item_id=item_id, status="DONE")
    assert response_update.status_code in [200, 204]

    # ===================== 5. MARK DONE =====================
    response_done = client.mark_item_done(item_id=item_id)
    assert response_done.status_code in [200, 204]

    # ===================== 6. DELETE =====================
    response_delete = client.delete_todo_item(habit_id=habit_id, item_id=item_id)
    assert response_delete.status_code in [200, 204, 404]

# def test_create_todo_items(access_token):
#
#     client = TodoClient(
#         base_url=Config.BASE_API_URL,
#         access_token=access_token
#     )
#
#     # ===================== 1. GET HABITS =====================
#     habits_response = client.get_habits()
#     assert habits_response.status_code == 200
#
#     habits = habits_response.json()
#     assert len(habits) > 0, "No habits found for user"
#
#     habit_id = habits[0]["id"]
#
#     # ===================== 2. GET TODO ITEMS =====================
#     response_get = client.get_todo_list(habit_id=habit_id)
#     assert response_get.status_code == 200
#
#     todo_items = response_get.json()
#     assert len(todo_items) > 0, "No todo items available for this habit"
#
#     valid_item_id = todo_items[0]["id"]
#
#     # ===================== 3. POST =====================
#     response = client.create_todo_items(
#         habit_id=habit_id,
#         body=[{"id": valid_item_id}],
#         lang="en"
#     )
#
#     # ===================== 4. ASSERT =====================
#     assert response.status_code == 201

# def test_create_todo_items(habit_id, body, status_code, access_token):
#     """Test creating to-do list items"""
#
#     client = TodoClient(
#         base_url=Config.BASE_API_URL,
#         access_token=access_token
#     )
#
#     response = client.create_todo_items(
#         habit_id=habit_id,
#         body=body,
#         lang="en"
#     )
#
#     if response.status_code == 201:
#         with allure.step("Validate response schema"):
#             parsed_data = response.json()
#             logger.info(parsed_data)
#
#             try:
#                 validate(instance=parsed_data, schema=todo_item_schema)
#             except ValidationError as e:
#                 allure.attach(
#                     str(e),
#                     name="Validation Error",
#                     attachment_type=allure.attachment_type.TEXT
#                 )
#                 pytest.fail(f"Schema validation failed: {e}")
#
#         with allure.step("Validate business logic"):
#             assert isinstance(parsed_data, list)
#             assert parsed_data[0]["status"] == "ACTIVE"
#
#     else:
#         assert response.status_code == status_code, \
#             f"Expected {status_code}, got {response.status_code}"
