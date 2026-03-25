Feature: New header

  As a registered user
  I want to click the "Form Habit" buttons on the About Us page
  So that I can navigate to the My Habit page

  Background:
    Given the user is on the main page
    And the user is logged in with valid credentials

  Scenario: Verify "Form Habit" buttons navigate to My Habit page
    When the user navigates to About Us page
    And the user clicks the first "Form Habit" button
    Then the My Habit page should be opened

    When the user navigates back to About Us page
    And the user clicks the second "Form Habit" button
    Then the My Habit page should be opened
