Feature: User Profile Cards
  As a logged-in user
  I want to browse cards of users who are in another user's friends list
  So that I can discover and interact with a broader network of users


  Background:
    Given I am a logged-in user
    And a target user exists with no cards
    And I navigate to the "Friend Profile" page of the target user
    And I open the "All Friends" tab

  Scenario: Display empty state message when a friend has no cards
    Then I should see the message "This user has no friends"

  Scenario: Verify friend card content in the target user friends list
    Then the user card should display the following elements:

      | field              |
      | Username           |
      | User City          |
      | "Add friend" button|

  Scenario: Viewing friend card in the target user friends list
    When I click on the first friend card in the list
    Then the URL should contain "/friends"
    And a user banner should be displayed on the page
