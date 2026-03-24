Feature: Navigate to Create Event page

  As a registered user
  I want to open the Create Event page from My Events
  So that I can create a new event

  Background:
    Given the user is signed in
    And the user is on the "My Space" page
    And the header navigation menu is visible

  Scenario: User opens the Create Event page from My Events tab
    When the user navigates to the My Events tab
    And the user clicks the "Add Event" link
    Then the Create Event page should open
    And the page header should be "Create event" or "Створити подію"
