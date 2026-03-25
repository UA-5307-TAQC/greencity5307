Feature: Habit Assignment Deletion API
  As a logged-in user
  I want to delete my assigned habits
  So that they are removed from my active list

  Background: User preparation
    Given the user is authorized
    And habit assign client is created

  Scenario: Successfully delete an assigned habit
    Given I have a clean state for habit ID 21
    And the habit with id 21 is already assigned to the user
    When I send a request to delete habit by assigned habit ID
    Then the response status code should be 200
    And the response body should be empty

  Scenario Outline: Try to delete a habit with invalid or non-existent ID
    When I send a request to delete habit by ID <habit_assign_id>
    Then the response status code should be <status_code>

    Examples:

      | habit_assign_id | status_code |
      | 0               | 404         |
      | "habitId"       | 400         |
