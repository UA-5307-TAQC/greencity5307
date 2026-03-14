Feature: Description field validation in habit update form

  Background:
    Given the user is logged in
    And the user is on the "Update Habit" page

  Scenario: Required field validation prevents saving
    When the user clears the "Habit Description" field
    And moves focus outside the field
    Then the description field shows a validation error
    And the "Save" button action is blocked
    And the message "This field is required" is displayed

  Scenario: Page refresh resets unsaved changes
    When the user clears the "Habit Description" field
    And refreshes the page
    Then the original description value from the database is restored