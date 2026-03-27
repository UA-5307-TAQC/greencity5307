Feature: Update profile privacy settings

  As a registered user
  I want to update my profile privacy settings
  So that my preferences are applied correctly

  Background:
    Given the user is signed in
    And the user is on the "My Space" page

  Scenario Outline: User updates profile privacy settings successfully
    When the user opens the Edit Profile page
    And the user updates location privacy to "<location_privacy>"
    And the user updates eco places privacy to "<eco_places_privacy>"
    And the user updates to-do privacy to "<todo_privacy>"
    Then the Save button should be enabled
    When the user clicks the Save button
    Then the user should be redirected to the profile page
    When the user reopens the Edit Profile page
    Then the location privacy should be "<location_privacy>"
    And the eco places privacy should be "<eco_places_privacy>"
    And the to-do privacy should be "<todo_privacy>"

  Examples:
    | location_privacy           | eco_places_privacy         | todo_privacy                |
    | Показувати мені та друзям  | Показувати мені та друзям  | Показувати мені та друзям  |
    | Показувати всім             | Показувати всім             | Показувати всім             |
    | Показувати тільки мені      | Показувати тільки мені      | Показувати тільки мені      |
