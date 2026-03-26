Feature: User Profile Functionality
  As a logged-in user
  I want to interact with my profile page
  So that I can manage my information and view relevant data


  Background:
    Given the user is signed in

  Scenario: Redirect to the Edit Profile page
    When I click the "Edit Profile" button
    Then I should be redirected to the "Edit Profile" page

  Scenario: Redirect to the My Friends page
    When I click the "See all" link on my profile banner
    Then I should be redirected to the appropriate friends page

  Scenario: Redirect to the Find Friends page
    When I click the "Add friends" button on my profile banner
    Then I should be redirected to the appropriate friends page

  Scenario: Display the current date on the calendar
    Then the profile calendar should match the system date:

      | Part  | Expected Value |
      | Day   | Current Day    |
      | Month | Current Month  |
      | Year  | Current Year   |
