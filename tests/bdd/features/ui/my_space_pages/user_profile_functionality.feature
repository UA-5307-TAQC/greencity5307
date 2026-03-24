@wip
Feature: User Profile Functionality
  As a logged-in user
  I want to interact with my profile page
  So that I can manage my information and view relevant data


  Background:
    Given I am logged in
    And I navigate to "My Space" page

  Scenario: Redirect to the Edit Profile page
    When I click the "Edit Profile" button
    Then I should be redirected to the "Edit Profile" page
    And the URL should contain "/edit"

  Scenario: Redirect to the Add Friends page
    When I click the "Add Friends" button
    Then I should be redirected to the "Add Friends" page
    And the URL should contain "/friends/recommended"

  Scenario: Display the current date on the calendar
    Then the profile calendar should match the system date:

      | Part  | Expected Value |
      | Day   | Current Day    |
      | Month | Current Month  |
      | Year  | Current Year   |
