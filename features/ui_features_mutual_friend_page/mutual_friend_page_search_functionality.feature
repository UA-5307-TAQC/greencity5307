Feature: Mutual friends search functionality

  Background:
    Given User A is logged in
    And User A and User B have mutual friends "Anna", "Denys", and "Petro"
    And User A opens User B's profile friends section
    And the "Mutual Friends" tab is active

  Scenario: Search filters mutual friends list
    When the user searches for "Denys"
    Then only "Denys" appears in the mutual friends list

  Scenario: Clearing search restores full friends list
    Given the user searched for "Denys"
    When the user clears the search field
    Then all mutual friends are visible