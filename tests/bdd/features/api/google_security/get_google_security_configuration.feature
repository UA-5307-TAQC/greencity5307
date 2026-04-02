Feature: Google Security Authentication

  As a user
  I want to validate Google security endpoint
  So that authentication works correctly

  Scenario Outline: Validate Google security with different parameters
    Given the user is authorized
    And I have GoogleSecurityClient
    When I send GET request to google security with project "<project_name>" and lang "<lang>"
    Then the response status code should be <status_code>
    And the response should match google security schema if status is 200
    And the response should contain "<message_type>" with value "<message>"

  Examples:
    | project_name | lang | status_code | message_type | message             |
    | GREENCITY   | en   | 200         |              |                     |
    | GREENCITY   | uk   | 200         |              |                     |
    |             | uk   | 404         | message      | Page is not found   |
