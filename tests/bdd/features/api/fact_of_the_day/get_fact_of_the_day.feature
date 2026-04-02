Feature: Fact of the Day API

  As an authenticated user
  I want to get a random fact of the day
  So that the response is valid and contains required data

  Background:
    Given the user is authorized

  Scenario: Get random fact of the day successfully
    When the user sends a request to get a random fact of the day
    Then the response status code should be 200
    And the response JSON should match the schema
    And the response should contain a valid id
    And the response should contain translations in "en" and "uk"
