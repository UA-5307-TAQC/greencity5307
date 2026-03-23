@wip
Feature: Friends page tabs navigation

  As a logged-in user
  I want to navigate through the tabs on the Friends page
  So that I can manage friends, requests, and find new friends

  Background:
    Given the user is logged in
    And the Friends page is opened

  Scenario: Navigate to My Friends tab
    When I click the "My Friends" button
    Then the My Friends tab should be opened

  Scenario: Navigate to Friend Requests tab
    When I click the "Friend Request" button
    Then the Friend Requests tab should be opened

  Scenario: Navigate to Find a Friend tab
    When I click the "Find a Friend" button
    Then the Find a Friend tab should be opened
