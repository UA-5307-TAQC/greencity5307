@wip
Feature: Click buttons in the vision card after sign in

  As a logged-in user
  I want to click buttons in the vision card
  So that I can navigate to the correct pages

  Background:
    Given the user is logged in
    And the About Us page is opened

  Scenario: Verify About Us page is opened
    Then the About Us page header should be visible

  Scenario: Click "Find Eco Places" button after sign in
    When I click the "Find Eco Places" button
    Then the Places page should be opened
    And I return to the About Us page

  Scenario: Click "Find People" button after sign in
    When I click the "Find People" button
    Then the Friends page should be opened
    And I return to the About Us page

  Scenario: Click "Get Inspired" button after sign in
    When I click the "Get Inspired" button
    Then the Eco News page should be opened
    And I return to the About Us page
