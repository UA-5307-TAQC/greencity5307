Feature: Update Eco News by ID

  As a user
  I want to update an eco news item by its ID
  So that the news content can be modified

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And EcoNewsClient is created using Config.BASE_API_URL

  Scenario Outline: Update eco news by id
    When I send a PUT request to "/<news_id>" with valid update data
    Then the response status code should be returned

    Examples:
      | news_id |
      | 1       |
      | 32      |
      | 2       |
      | 77      |
      | 90      |

  Scenario: Successfully update eco news
    Given a valid eco news id and valid update data
    When I send a PUT request to "/<news_id>"
    And the response status code is 201
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission to update eco news
    Given a valid eco news id
    When I send a PUT request to "/<news_id>"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Eco news does not exist
    Given a non-existing eco news id
    When I send a PUT request to "/<news_id>"
    And the response status code is 404
    Then the response body should contain message "Eco new doesn't exist by this id: {news_id}"

  Scenario: Unexpected status code
    When I send a PUT request to "/<news_id>"
    And the response status code is not one of [201, 400, 404]
    Then the test should fail with message "Other error"
