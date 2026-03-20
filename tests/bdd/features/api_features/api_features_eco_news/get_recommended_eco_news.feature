Feature: Get recommended eco news

  As a client of the Eco News API
  I want to retrieve recommended eco news for a given news item
  So that I can suggest related articles to users

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And EcoNewsClient is created using Config.BASE_API_URL

  Scenario Outline: Retrieve recommended eco news
    When I send a GET request to "/<news_id>/recommended"
    Then the response status code should be captured

    Examples:
      | news_id |
      | 1       |
      | 32      |
      | 2       |
      | 77      |
      | 90      |

  Scenario: Successfully retrieve recommended eco news
    Given a valid news ID
    When I send a GET request to "/<news_id>/recommended"
    And the response status code is 200
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission
    Given a valid news ID
    When I send a GET request to "/<news_id>/recommended"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Eco news not found
    Given a non-existing news ID
    When I send a GET request to "/<news_id>/recommended"
    And the response status code is 404
    Then the response body should contain message "Eco new doesn't exist by this id: {news_id}"

  Scenario: Forbidden access
    Given a request without proper authorization
    When I send a GET request to "/<news_id>/recommended"
    And the response status code is 403
    Then the response body should contain message "Forbidden access"

  Scenario: Internal server error
    Given the server encounters an unexpected condition
    When I send a GET request to "/<news_id>/recommended"
    And the response status code is 500
    Then the response body should contain message "Internal Server Error"

  Scenario: Unexpected status code
    When I send a GET request to "/<news_id>/recommended"
    And the response status code is not one of [200, 400, 403, 404, 500]
    Then the test should fail with message "Other error"
