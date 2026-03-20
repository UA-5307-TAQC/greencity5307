Feature: Create eco news with invalid data

  As a logged-in user
  I want the system to validate eco news fields
  So that invalid news cannot be submitted

  Background:
    Given the user is logged in
    And the "Create Eco News" page is open

  Scenario: Verify Create News page header
    Then the page header should be visible

  Scenario: Verify submit button initial state
    Then the submit button should be disabled

  Scenario: Attempt to create eco news with invalid data
    When I enter an empty title
    And I enter empty tags
    And I enter source "Green Blog"
    And I enter content with less than 300 characters
    And I click the submit button
    Then the form should not be submitted
    And the submit button should remain disabled
    And the "Create Eco News" page should still be open
