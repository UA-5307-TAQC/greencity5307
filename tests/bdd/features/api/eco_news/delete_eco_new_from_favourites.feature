Feature: Delete Eco News from Favorites

  As an authorized user
  I want to remove eco news from favorites
  So that I can manage my saved content

  Scenario Outline: Delete eco news from favorites by id
    Given I am an authorized user
    When I send request to delete eco news with id "<news_id>" from favorites
    Then the response status code should be <status_code>
    And the response message should be <message>

    Examples:
      | news_id | status_code | message                                      |
      | 1       | 404         | Eco new doesn't exist by this id: 1          |
      | 32      | 400         | This eco new is not in favorites.            |
      | 2       | 404         | Eco new doesn't exist by this id: 2          |
      | 77      | 404         | Eco new doesn't exist by this id: 77         |
      | 90      | 400         | This eco new is not in favorites.            |
