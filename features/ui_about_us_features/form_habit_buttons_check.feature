Feature: About Us page "Form Habit" buttons verification

  As a logged-in user
  I want to verify the "Form Habit" buttons
  So that they navigate correctly to the My Habits page

  Background:
    Given the user is logged in
    And the About Us page is opened

  Scenario: Click first "Form Habit" button
    When I click the first "Form Habit" button
    Then the My Habits page should be opened
    And I return to the About Us page

  Scenario: Click second "Form Habit" button
    When I click the second "Form Habit" button
    Then the My Habits page should be opened
    And I return to the About Us page
