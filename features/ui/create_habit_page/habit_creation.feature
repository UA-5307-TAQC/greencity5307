Feature: Habit Creation
  As a logged-in user
  I want to create new habits
  So that I can track my personal progress


  Background:
    Given I am logged in
    And I navigate to the "Create Habit" page

  Scenario: Successfully create a habit with mandatory fields
    When I fill in the "Title" field with "Test title"
    And I click on the "Testing" tag chip
    And I fill in the "Description" textarea with "Test habit description"
    Then the "Add Habit" button should be clickable
    When I click the "Add Habit" button
    Then I should be redirected to the "All Habits" page
    And the first habit in the list should have the title "Test title"
    When I click on the habit "Test title"
    And I click the "Delete" button

  Scenario: Validation of mandatory "Title" field
    When I fill in the "Description" textarea with "Test habit description"
    And I click on the "Testing" tag chip
    And I click the "Add Habit" button
    Then I should see an error message for "Title" field
    And the "Add Habit" button shouldn't be clickable

  Scenario: Validation of mandatory "Description" textarea
    When I fill in the "Title" field with "Test title"
    And I click on the "Testing" tag chip
    And I click the "Add Habit" button
    Then I should see an error message for "Description" textarea
    And the "Add Habit" button shouldn't be clickable
