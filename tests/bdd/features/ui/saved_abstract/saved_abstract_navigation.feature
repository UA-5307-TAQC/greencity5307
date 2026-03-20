# Documentation-only feature file for saved abstract navigation.
#
# This file is intentionally limited to comments and does not define any
# executable Gherkin Features or Scenarios. It serves as high-level
# documentation for expected navigation behavior in the "saved abstracts"
# area of the UI.
#
# If automated BDD tests are desired in the future, either:
#   - Add a BDD runner (e.g., pytest-bdd or behave) and corresponding
#     step definitions, then move executable scenarios into a dedicated
#     test-oriented .feature file, or
#   - Re-implement the scenarios as pytest tests that run in the
#     existing CI configuration.
#
# Example (non-executable) behavior description:
# - Users can open the "Saved abstracts" section from the main navigation.
# - From the list of saved abstracts, selecting an item navigates to the
#   abstract details page.
# - The browser "Back" button returns to the saved abstracts list while
#   preserving any active filters or sort order.
#
# NOTE: Do not add `Feature:` or `Scenario:` keywords here unless you
# also configure an appropriate BDD runner in CI.
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
