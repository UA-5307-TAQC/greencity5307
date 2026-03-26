Feature: API Access Control
  As an unauthorized user
  I should not be able to perform protected actions
  To ensure system security

  Background: User preparation
    Given habit assign client without authorization is created

  Scenario: Try to assign a habit without authorization
    When I send a request to assign habit ID 21
    Then the response status code should be 401

  Scenario: Try to delete a habit assign without authorization
    When I send a request to delete habit by ID 21
    Then the response status code should be 401

  Scenario: Try to get all assigned habit without authorization
    When I send a request to get all habit assignments with "en"
    Then the response status code should be 401
