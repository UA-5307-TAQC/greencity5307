Feature: Cancel habit update

  Background:
    Given the user is logged in
    And the user opens the "Update Habit" page

  Scenario: Verify cancel button discards changes
    When the user edits the habit name to "Test Cancel"
    And changes the visibility to "Private"
    And clicks the "Cancel" button
    Then the user is redirected to the "My Habits" page

  Scenario: Verify habit data remains unchanged after cancel
    Given a habit named "Test Habit" with visibility "Public" exists
    And the user opens the "Update Habit" page for habit "Test Habit"
    When the user edits the habit name to "Test Cancel"
    And changes the visibility to "Private"
    And clicks the "Cancel" button
    And the user reopens the habit "Test Habit"
    Then the habit name equals "Test Habit"
