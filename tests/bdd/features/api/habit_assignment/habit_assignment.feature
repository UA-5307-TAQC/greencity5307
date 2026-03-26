Feature: Habit Assignment API
  As a logged-in user
  I want to assign habits to myself
  So that I can track my progress

  Background: User preparation
    Given the user is authorized
    And habit assign client is created

  Scenario Outline: Successfully assign a valid habit
    Given I have a clean state for habit ID <habit_id>
    When I send a request to assign habit ID <habit_id>
    Then the response status code should be 201
    And the response JSON should match the schema
    And the habit assignment is removed

    Examples:

      | habit_id |
      | 1        |
      | 21       |


  Scenario: Try to assign a non-existent habit
    When I send a request to assign habit ID -3
    Then the response status code should be 404

  Scenario: Try to assign a habit that is already assigned
    Given the habit with id 21 is already assigned to the user
    When I send a request to assign habit ID 21
    Then the response status code should be 400
    And the habit assignment is removed
