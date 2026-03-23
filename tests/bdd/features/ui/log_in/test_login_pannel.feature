@wip
Feature: Sign-In Modal Validation
  As a user attempting to log in
  I want to be prompted when I leave mandatory fields empty
  So that I know valid credentials are required to proceed

  Background:
    Given the user has navigated to the application URL
    And the "Welcome back!" modal is open and visible
    And both the "Email" and "Password" fields are empty

  Scenario: Display validation errors for empty mandatory fields
    When the user clicks on the "Email" field and then clicks outside of it
    Then a red error message "Email is required." should appear below the Email field
    When the user clicks on the "Password" field and then clicks outside of it
    Then a red error message "This field is required" should appear below the Password field
