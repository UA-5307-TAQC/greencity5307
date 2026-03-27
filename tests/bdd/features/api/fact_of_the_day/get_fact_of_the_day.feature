Feature: Fact of the Day API
  As an authenticated user
  I want to get a random fact of the day
  So that the response is valid and matches the schema

  Background:
    Given the user has a valid access token

  Scenario: Get random fact of the day and validate schema
    When the user requests a random fact of the day
    Then the response status code should be 200
    And the response should match the fact of the day schema
    And the response should contain a valid "id"
    And the response should contain translations in "en" and "uk"
