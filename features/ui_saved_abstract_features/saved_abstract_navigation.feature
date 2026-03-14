Feature: Saved page tabs navigation

  As a logged-in user
  I want to navigate through the tabs on the Saved page
  So that I can view my saved events, places, and news

  Background:
    Given the user is logged in
    And the Saved page is opened

  Scenario: Verify Saved page tabs are visible
    Then all tabs on the Saved page should be visible

  Scenario: Navigate to Saved Events tab
    When I go to the Saved Events tab
    Then the Saved Events tab should be opened

  Scenario: Navigate to Saved Places tab
    When I go to the Saved Places tab
    Then the Saved Places tab should be opened

  Scenario: Navigate to Saved News tab
    When I go to the Saved News tab
    Then the Saved News tab should be opened
