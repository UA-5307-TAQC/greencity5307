Feature: Delete Eco News by ID

  As a user
  I want to delete an eco news item by its ID
  So that unnecessary or outdated news can be removed

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And EcoNewsClient is created using Config.BASE_API_URL

  Scenario Outline: Delete eco news by id
    When I send a DELETE request to "/eco-news/<news_id>"
    Then the response status code should be returned

    Examples:
      | news_id |
      | 1       |
      | 32      |
      | 2       |
      | 77      |
      | 90      |

  Scenario: Successfully delete eco news
    Given a valid eco news id
    When I send a DELETE request to "/eco-news/{news_id}"
    And the response status code is 200
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission to delete eco news
    Given a valid eco news id
    When I send a DELETE request to "/eco-news/{news_id}"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Eco news does not exist
    Given a non-existing eco news id
    When I send a DELETE request to "/eco-news/{news_id}"
    And the response status code is 404
    Then the response body should contain message "Eco new doesn't exist by this id: {news_id}"

  Scenario: Unexpected status code
    When I send a DELETE request to "/eco-news/{news_id}"
    And the response status code is not one of [200, 400, 404]
    Then the test should fail with message "Other error"
