"""Validation of creating to-do list items"""
import allure
import pytest
from jsonschema import validate, ValidationError

from clients.to_do_list_client import TodoClient
from data.config import Config
from schemas.to_do_list_schema import todo_item_schema
from utils.logger import logger


# @pytest.mark.parametrize(
#     "habit_id, body, status_code",
#     [
#         (1, [{"id": 2}], 201),
#         (99999, [{"id": 1}], 400),
#     ]
# )

@allure.feature("ToDoList")
@allure.story("Create to-do list items")
@allure.title("Create to-do list items for user")
def test_create_todo_items(access_token):

    client = TodoClient(
        base_url=Config.BASE_API_URL,
        access_token=access_token
    )

    # ===================== 1. GET HABITS =====================
    habits_response = client.get_habits()
    assert habits_response.status_code == 200

    habits = habits_response.json()
    assert len(habits) > 0, "No habits found for user"

    habit_id = habits[0]["id"]

    # ===================== 2. GET TODO ITEMS =====================
    response_get = client.get_todo_list(habit_id=habit_id)
    assert response_get.status_code == 200

    todo_items = response_get.json()
    assert len(todo_items) > 0, "No todo items available for this habit"

    valid_item_id = todo_items[0]["id"]

    # ===================== 3. POST =====================
    response = client.create_todo_items(
        habit_id=habit_id,
        body=[{"id": valid_item_id}],
        lang="en"
    )

    # ===================== 4. ASSERT =====================
    assert response.status_code == 201

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
