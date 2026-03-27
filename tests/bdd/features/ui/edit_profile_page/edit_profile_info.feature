Feature: Update basic profile information

  As a registered user
  I want to update my profile information
  So that my personal data is saved correctly

  Background:
    Given the user is signed in
    And the user is on the "My Space" page

  Scenario Outline: User updates basic profile information successfully
    When the user opens the Edit Profile page
    And the user updates name to "<name>"
    And the user updates city to "<city>"
    And the user updates credo to "<credo>"
    Then the Save button should be enabled
    When the user clicks the Save button
    Then the user should be redirected to the profile page
    When the user reopens the Edit Profile page
    Then the name should be "<name>"
    And the city should be "<city>, Україна"

  Examples:
    | name       | city    | credo                    |
    | Hlib       | Київ    | I sort waste every day  |
    | Oleksandr  | Харків  | Save nature every day   |
