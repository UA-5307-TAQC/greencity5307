Feature: Like or Unlike Eco News

  As an authorized user
  I want to like or remove like from eco news
  So that I can manage my reactions

  Scenario Outline: Like or unlike eco news by id
    Given I am an authorized user
    When I send request to like or unlike eco news with id "<news_id>"
    Then the response status code should be <status_code>
    And the response message should be <message>

    Examples:
      | news_id | status_code | message |
      | 1       | 404         |Eco new doesn't exist by this id: 1         |
      | 32      | 200         |         |
      | 2       | 404         |Eco new doesn't exist by this id: 2         |
      | 77      | 404         |Eco new doesn't exist by this id: 77         |
      | 90      | 200         |         |
