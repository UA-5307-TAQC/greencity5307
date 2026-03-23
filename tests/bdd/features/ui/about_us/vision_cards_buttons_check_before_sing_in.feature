@wip
Feature: Click buttons in the vision card before sign in

  As a user
  I want to click buttons in the vision card
  So that I can see the expected modals or pages even before signing in

  Background:
    Given the user is logged in
    And the About Us page is opened

  Scenario: Verify About Us page is opened
    Then the About Us page header should be visible

  Scenario: Click "Find Eco Places" button before sign in
    When I click the "Find Eco Places" button
    Then the Sign In modal should be opened
    And I return to the About Us page

  Scenario: Click "Find People" button before sign in
    When I click the "Find People" button
    Then the Sign In modal should be opened
    And I return to the About Us page

  Scenario: Click "Get Inspired" button before sign in
    When I click the "Get Inspired" button
    Then the Eco News page should be opened
    And I return to the About Us page
