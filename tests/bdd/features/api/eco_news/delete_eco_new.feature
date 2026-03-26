Feature: Delete Eco News

  As an authorized user
  I want to delete eco news by id
  So that I can remove unwanted content

  Scenario Outline: Delete eco news by id with invalid or restricted access
    Given I am an authorized user
    When I send request to delete eco news with id "<news_id>"
    Then the response status code should be <status_code>
    And the response message get/delete request should be "<message>"

    Examples:
      | news_id | status_code | message                                             |
      | 1       | 404         | Eco new doesn't exist by this id: 1                 |
      | 32      | 400         | Current user has no permission for this action      |
      | 2       | 404         | Eco new doesn't exist by this id: 2                 |
      | 77      | 404         | Eco new doesn't exist by this id: 77                |
      | 90      | 400         | Current user has no permission for this action      |
