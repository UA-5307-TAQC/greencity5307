@wip
Feature: Mutual friends API when users have no mutual friends

  Background:
    Given User A is authenticated
    And User D exists in the system
    And User A and User D have no mutual friends

  Scenario: API returns empty mutual friends list
    When User A sends a GET request to "/users/{userD_id}/mutual-friends"
    Then the response status code should be 200
    And the response body contains "count" equal to 0
    And the response body contains an empty "mutualFriends" array

  Scenario: API response structure validation
    When User A requests mutual friends for User D
    Then the response body should contain fields:
      | field          |
      | count          |
      | mutualFriends  |
    And "mutualFriends" should be an empty list

  Scenario: Mutual friends count consistency
    When User A requests mutual friends for User D
    Then the value of "count" should equal the length of "mutualFriends"
    And the value should be 0
