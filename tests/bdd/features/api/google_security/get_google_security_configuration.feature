@wip
Feature: Get Google Security configuration

  As a client of the Google Security API
  I want to retrieve Google Security configuration by project name and language
  So that the correct security settings are returned

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And SocialNetworkClient is created using Config.BASE_API_URL

  Scenario Outline: Get Google Security configuration
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    Then the response status code should be captured

    Examples:
      | project_name | lang |
      | GREENCITY    | en   |
      | GREENCITY    | uk   |

  Scenario: Successfully retrieve Google Security configuration
    Given a valid project name and language
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    And the response status code is 200
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission
    Given a valid project name and language
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Page not found
    Given an invalid project name or language
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    And the response status code is 404
    Then the response body should contain message "Page is not found"

  Scenario: Forbidden access
    Given a request without proper authorization
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    And the response status code is 403
    Then the response body should contain message "Forbidden access"

  Scenario: Internal server error
    Given the server encounters an unexpected condition
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    And the response status code is 500
    Then the response body should contain message "Internal Server Error"

  Scenario: Unexpected status code
    When I send a GET request to "/googleSecurity" with project "<project_name>" and language "<lang>"
    And the response status code is not one of [200, 400, 403, 404, 500]
    Then the test should fail with message "Other error"
