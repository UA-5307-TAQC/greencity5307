# pylint: disable=not-callable, unused-argument
"""
.. module:: Header navigation
    :platform: Unix
    :synopsis: """
from behave import given, when, then

from data.config import Config
from clients.habit_assign_client import HabitAssignClient
from schemas.habits.assigned_habit_schema import assigned_habit_schema
from schemas.habits.all_habit_assignments_schema import all_habit_assignments_schema


def get_assigned_id(client, habit_id: int):
    """Gets assigned habit id"""
    response = client.get_all_habit_assignments_for_current_user()
    assert response.status_code == 200, (
        f"Failed to get assigned habits: {response.status_code} - {response.text}"
    )
    for habit in response.json():
        if habit["habit"]["id"] == habit_id:
            return habit["id"]
    return None


@given('habit assign client without authorization is created')
def create_habit_assign_client_without_token(context):
    """Initializes a habit assigned client without authorization"""
    context.client = HabitAssignClient(base_url=Config.BASE_API_URL)


@given('habit assign client is created')
def create_habit_assign_client(context):
    """Initializes a habit assigned client with authorization"""
    access_token = context.auth_token
    context.client = HabitAssignClient(base_url=Config.BASE_API_URL, access_token=access_token)


@given('I have a clean state for habit ID {habit_id:d}')
def clean_habit(context, habit_id):
    """Deletes an assigned habit by habit assign id"""
    assigned_id = get_assigned_id(context.client, habit_id)
    if assigned_id:
        context.client.delete_habit_assign(assigned_id)
    context.habit_id = habit_id


@given('the habit with id {habit_id:d} is already assigned to the user')
def pre_assign_habit(context, habit_id):
    """Pre-assignes a habit by id"""
    response = context.client.assign_habit_with_default_properties(habit_id)
    assert response.status_code == 201
    context.habit_id = habit_id


@when('I send a request to get all habit assignments with "{language}"')
def send_get_all_habit_assignments_for_current_user_request(context, language):
    """Send request to get all habit assignments"""
    context.response = context.client.get_all_habit_assignments_for_current_user(language)
    context.schema = all_habit_assignments_schema


@when('I send a request to assign habit ID {habit_id:d}')
def send_post_request_to_assign_habit(context, habit_id):
    """Assignes a habit by id"""
    context.response = context.client.assign_habit_with_default_properties(habit_id)
    context.schema = assigned_habit_schema


@when('I send a request to delete habit by assigned habit ID')
def send_delete_habit_assignment_request(context):
    """Remove the assigned habit"""
    assigned_id = get_assigned_id(context.client, context.habit_id)
    response = context.client.delete_habit_assign(assigned_id)
    context.response = response


@when('I send a request to delete habit by ID {habit_assign_id}')
def send_invalid_delete_habit_assignment_request(context, habit_assign_id):
    """Remove the assigned habit by invalid ID"""
    if habit_assign_id.isdigit():
        habit_assign_id = int(habit_assign_id)
    response = context.client.delete_habit_assign(habit_assign_id)
    context.response = response


@then('the habit assignment is removed')
def remove_habit_assignment(context):
    """Remove the assigned habit"""
    assigned_id = get_assigned_id(context.client, context.habit_id)
    response = context.client.delete_habit_assign(assigned_id)
    assert response.status_code == 200
