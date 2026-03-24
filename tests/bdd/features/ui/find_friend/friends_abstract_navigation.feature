Feature: Friends page tabs navigation

  As a signed-in user
  I want to navigate through tabs on the Friends page
  So that I can view My Friends, Find Friends, and Friend Requests

  Background:
    Given the user is on the main page
    And the user is logged in with valid credentials


  Scenario: Navigate through Friends page tabs
    When the user navigates to My Space page
    And the user goes to the Friends tab
    Then the Friends page should be opened

    When the user goes to "My Friends" tab at friends page
    Then the "My Friends" tab at friends page should be active

    When the user goes to "Find Friends" tab at friends page
    Then the "Find Friends" tab at friends page should be active

    When the user goes to "Friend Requests" tab at friends page
    Then the "Friend Requests" tab at friends page should be active
