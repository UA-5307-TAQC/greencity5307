@wip
Feature: Mutual friends visibility on user profile

  Background:
    Given User A is logged into the system
    And User B exists in the system
    And User C is a friend of both User A and User B
    And User A is on User B's profile page

  Scenario: View mutual friends between users
    When the user opens the "Friends" section on User B's profile
    And selects "All Friends"
    Then the list of User B's friends is displayed
    And the tabs "All Friends" and "Mutual Friends" are visible

  Scenario: Verify mutual friends counter
    When the user views the "Mutual Friends" tab
    Then the mutual friends counter displays "1"

  Scenario: Display mutual friends list
    When the user clicks on the "Mutual Friends" tab
    Then the tab becomes active
    And User C is displayed in the friends list
    And User C's profile picture is visible

  Scenario: Verify scrolling or pagination of friends list
    Given the mutual friends list is displayed
    When the user scrolls the friends list
    Then more mutual friends are visible in the list than before scrolling

  Scenario: Verify mutual friends tab after page refresh
    When the user refreshes the page
    Then the profile page reloads successfully
    And the "Mutual Friends" tab is still accessible
