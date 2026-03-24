Feature: Create Eco News with invalid data

  As a registered user
  I want to be prevented from creating eco news with invalid data
  So that incorrect information is not submitted

  Background:
    Given the user is on the main page
    And the user is logged in with valid credentials


  Scenario: Attempt to create eco news with invalid data
    When the user navigates to Eco News page
    And the user clicks on create news button
    Then the Create Eco News page should be opened

    When the user fills the eco news form with invalid data
    Then the form fields should contain entered invalid data

    When the user tries to submit the eco news form
    Then the Create Eco News page should remain opened after submission
    And the submit button should be disabled
