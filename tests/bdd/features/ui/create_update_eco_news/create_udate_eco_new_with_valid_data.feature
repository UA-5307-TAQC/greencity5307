@wip
Feature: Create eco news with valid data

  As a logged-in user
  I want to create eco news with valid information
  So that it appears in the Eco News list

  Background:
    Given the user is logged in
    And the CreateUpdateEcoNewsPage is open

  Scenario: Verify Create Eco News page header
    Then the page header should be visible

  Scenario: Verify submit button initial state
    Then the submit button should be disabled

  Scenario: Successfully create eco news with valid data
    When I enter title "Save the Planet"
    And I enter tags "Eco, Nature"
    And I enter source "Green Blog"
    And I enter content with more than 300 characters
    And I click the submit button
    Then the form should be submitted
    And a success message should be displayed
    And the created eco news should appear in the Eco News list
