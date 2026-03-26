Feature: Add Eco News to Favorites

  As an authenticated user
  I want to add eco news to favorites
  So that I can save interesting articles

  Scenario Outline: Add eco news to favorites by id
    Given I am an authorized user
    When I send request to add eco news with id "<news_id>" to favorites
    Then the response status code should be <status_code>
    And the response message post request should be "<message>"

    Examples:
      | news_id | status_code | message                                             |
      | 1       | 404         | Eco new doesn't exist by this id: 1                 |
      | 32      | 400         | User has already added this eco new to favorites.  |
      | 2       | 404         | Eco new doesn't exist by this id: 2                 |
      | 77      | 404         | Eco new doesn't exist by this id: 77                |
      | 90      | 400         | User has already added this eco new to favorites.  |
