Feature: Get Eco News Summary

  As an authorized user
  I want to retrieve eco news summary by id
  So that I can view a short version of the article

  Scenario Outline: Get eco news summary by id
    Given the user is authorized
    And Get EcoNewsClient
    When I send request to get summary of eco news with id "<news_id>"
    Then the response status code should be <status_code>
    And the response message should be <message>

    Examples:
      | news_id | status_code | message                                      |
      | 1       | 404         | Eco new doesn't exist by this id: 1          |
      | 32      | 200         |                                              |
      | 2       | 404         | Eco new doesn't exist by this id: 2          |
      | 77      | 404         | Eco new doesn't exist by this id: 77         |
      | 90      | 200         |                                              |
