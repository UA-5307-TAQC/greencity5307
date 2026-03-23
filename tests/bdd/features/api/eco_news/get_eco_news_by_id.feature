@wip
Feature: Retrieve eco news by ID

  Scenario Outline: Validate eco news retrieval by ID with different languages
    Given the API client is configured with the base API URL
    When the client sends a request to get eco news with id "<news_id>" and language "<lang>"
    Then the API should return a valid response depending on the request
    And if the status code is 200 the response body should match the eco news schema
    And if the status code is 400 the response message should indicate an incorrect language
    And if the status code is 404 the response message should indicate that the eco news with the given id does not exist

    Examples:
      | news_id | lang      |
      | 1       | en        |
      | 2       | en        |
      | 3       | en        |
      | 17      | en        |
      | 77      | en        |
      | 734     | en        |
      | 4044    | en        |
      | 1       | uk        |
      | 2       | uk        |
      | 3       | uk        |
      | 17      | uk        |
      | 77      | uk        |
      | 734     | uk        |
      | 4044    | uk        |
      | 1       | not-exist |
      | 2       | not-exist |
      | 3       | not-exist |
      | 17      | not-exist |
      | 77      | not-exist |
      | 734     | not-exist |
      | 4044    | not-exist |
