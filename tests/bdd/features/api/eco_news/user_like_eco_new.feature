@wip
Feature: Check if user liked eco news

  As a client of the Eco News API
  I want to check whether a specific user liked an eco news item
  So that I can display the correct like state

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And EcoNewsClient is created using Config.BASE_API_URL

  Scenario Outline: Check if user liked eco news by id
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    Then the response status code should be captured

    Examples:
      | eco_news_id | user_id |
      | 1           | 10      |
      | 32          | 10      |
      | 2           | 10      |
      | 77          | 15      |
      | 90          | 20      |

  Scenario: Successfully check if user liked eco news
    Given a valid eco news id and user id
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    And the response status code is 200
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission to check like status
    Given a valid eco news id and user id
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Eco news does not exist
    Given a non-existing eco news id
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    And the response status code is 404
    Then the response body should contain message "Eco new doesn't exist by this id: {eco_news_id}"

  Scenario: Forbidden access
    Given a request without proper authorization
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    And the response status code is 403
    Then the response body should contain message "Forbidden access"

  Scenario: Internal server error
    Given the server encounters an unexpected condition
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    And the response status code is 500
    Then the response body should contain message "Internal Server Error"

  Scenario: Unexpected status code
    When I send a GET request to "/<eco_news_id>/likes/<user_id>"
    And the response status code is not one of [200, 400, 403, 404, 500]
    Then the test should fail with message "Other error"
