Feature: Get All Habit Assignments for current user API
  As a logged-in user
  I want to retrieve my list of assigned habits
  So that I can review and track my daily progress

  Background: User preparation
    Given the user is authorized
    And habit assign client is created

  Scenario Outline: Get habit assignments for current user with supported language codes
    Given I have a clean state for habit ID 25
    And the habit with id 25 is already assigned to the user
    When I send a request to get all habit assignments with <language>
    Then the response status code should be 200
    And the response JSON should match the schema
    And the habit assignment is removed

    Examples:

      | language |
      | "en"     |
      | "uk"     |


  Scenario: Get habit assignments for current user with incorrect language code
    When I send a request to get all habit assignments with "test"
    Then the response status code should be 400
