Feature: Get User DTO by principal (email from access token)

  Scenario: Get user dto with valid access token
    Given the user is authorized
    And created UserClient
    When I send request to get user dto by principal
    Then validate schema for user dto by principal
    And validate if user access is forbidden
    And user response status code should be successful or forbidden


  Scenario: Get user dto with invalid access token
    Given I have invalid access token
    And created UserClient
    When I send request to get user dto by principal
    Then validate if user is unauthorised
    And user response status code should be unauthorized
