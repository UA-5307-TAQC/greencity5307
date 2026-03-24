Feature: Create Eco News

  As a registered user
  I want to create eco news
  So that I can share environmental updates

  Background:
    Given the user is logged in with valid credentials
    And the user is on the main page


  Scenario: Create eco news with valid data
    When the user navigates to Eco News page
    And the user clicks on create news button
    Then the Create Eco News page should be opened

    When the user fills the eco news form with valid data
    Then the form fields should contain entered data

    When the user submits the eco news form
    Then the Create Eco News page should remain opened after submission
