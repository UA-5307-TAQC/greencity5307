Feature: User account dropdown functionality

  Background:
    Given the user is successfully logged in
    And the header is visible

  Scenario: Display logged-in user information in header
    Then the user avatar or username is displayed in the top-right corner
    And the displayed username corresponds to the logged-in account

  Scenario: User opens account dropdown menu
    When the user clicks on the username or avatar in the header
    Then the account dropdown menu expands
    And the "Profile" option is visible
    And the "Sign out" option is visible

  Scenario: User navigates to profile page from dropdown
    Given the account dropdown menu is open
    When the user clicks on "Profile"
    Then the user is redirected to the Profile page
    And the profile/settings page loads successfully

  Scenario: User signs out from the account
    Given the user is on the Profile page
    When the user clicks on the username or avatar in the header
    And selects "Sign out"
    Then the user is redirected to the homepage or login page
    And the header displays the "Sign in" button instead of the user avatar