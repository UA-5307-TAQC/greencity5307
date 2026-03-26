Feature: Get Recommended Eco News

  As an authorized user
  I want to get recommended eco news by id
  So that I can discover similar content

  Scenario Outline: Get recommended eco news by id
    Given I am an authorized user
    When I send request to get recommended eco news with id "<news_id>"
    Then the response status code should be <status_code>

    Examples:
      | news_id | status_code |
      | 1       | 200         |
      | 32      | 200         |
      | 2       | 200         |
      | 77      | 200         |
      | 90      | 200         |
