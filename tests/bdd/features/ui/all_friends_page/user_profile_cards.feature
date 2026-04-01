Feature: User Profile Cards
  As a logged-in user
  I want to browse cards of users who are in another user's friends list
  So that I can discover and interact with a broader network of users


  Background:
    Given the user is signed in

  Scenario: Display empty state text when a friend has no cards
    Given a target user has no friend cards on the "All Friends" page
    Then I should see the "This user has no friends" text

  Scenario: Verify friend card content in the target user friends list
    Given a target user has friend cards on the "All Friends" page
    Then the friend card should display the following elements

      | Element              |
      | Username             |
      | User City            |
      | "Add friend" button  |

  Scenario: Viewing friend card in the target user friends list
    Given a target user has friend cards on the "All Friends" page
    When I click on the first friend card in the list
    Then the URL should contain "/friends"
    And a user banner should be displayed on the page
