Feature: Dislike Eco News by ID

  As a user
  I want to dislike an eco news item by its ID
  So that I can remove my like from the news

  Background:
    Given the environment variable BASE_API_URL is configured
    And EcoNewsClient is created using Config.BASE_API_URL

  Scenario Outline: Dislike eco news by id
    When I send a POST request to "/<news_id>/dislikes"
    Then the response status code should be captured

  Examples:
    | news_id |
    | 1       |
    | 32      |
    | 2       |
    | 77      |
    | 90      |

  Scenario: Successful dislike request
    Given a valid eco news id
    When I send a POST request to "/<news_id>/dislikes"
    And the response status code is 201
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission to dislike eco news
    Given a valid eco news id
    When I send a POST request to "/<news_id>/dislikes"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Eco news does not exist
    Given a non-existing eco news id
    When I send a POST request to "/<news_id>/dislikes"
    And the response status code is 404
    Then the response body should contain message "Eco new doesn't exist by this id: {news_id}"

  Scenario: Forbidden access
    Given a request without proper authorization
    When I send a POST request to "/<news_id>/dislikes"
    And the response status code is 403
    Then the response body should contain message "Forbidden access"

  Scenario: Internal server error
    Given the server encounters an unexpected condition
    When I send a POST request to "/<news_id>/dislikes"
    And the response status code is 500
    Then the response body should contain message "Internal Server Error"

  Scenario: Unexpected status code
    When I send a POST request to "/<news_id>/dislikes"
    And the response status code is not one of [200, 400, 403, 404, 500]
    Then the test should fail with message "Other error"
