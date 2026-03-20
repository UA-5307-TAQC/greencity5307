Feature: Delete social network by id

  As a client of the Social Network API
  I want to delete a social network by its id
  So that unused or incorrect networks can be removed

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And SocialNetworkClient is created using Config.BASE_API_URL

  Scenario Outline: Delete social network by id
    When I send a DELETE request to "/social-networks"
    Then the response status code should be captured

    Examples:
      | network_id |
      | 1          |
      | 2          |
      | 3          |
      | 4          |

  Scenario: Successfully delete social network
    Given a valid social network id
    When I send a DELETE request to "/social-networks"
    And the response status code is 200
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission to delete social network
    Given a valid social network id
    When I send a DELETE request to "/social-networks"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Social network not found
    Given a non-existing social network id
    When I send a DELETE request to "/social-networks"
    And the response status code is 404
    Then the response body should contain message "Page is not found"

  Scenario: Forbidden access
    Given a request without proper authorization
    When I send a DELETE request to "/social-networks"
    And the response status code is 403
    Then the response body should contain message "Forbidden access"

  Scenario: Internal server error
    Given the server encounters an unexpected condition
    When I send a DELETE request to "/social-networks"
    And the response status code is 500
    Then the response body should contain message "Internal Server Error"

  Scenario: Unexpected status code
    When I send a DELETE request to "/social-networks"
    And the response status code is not one of [200, 400, 403, 404, 500]
    Then the test should fail with message "Other error"
