@TC-0033
Feature: Habit Duration Customization
  As a GreenCity user
  I want to adjust the duration of my habits using a slider
  So that I can set custom timelines for my goals

  Background:
    Given the user is successfully logged in
    And the user has opened a habit card
    And the duration slider is initially set to the default value of "7"

  Scenario: Slider stops at the boundaries (Min and Max)
    When the user drags the slider handle to the maximum right position
    Then the text indicator should display the maximum value of "56"
    When the user drags the slider handle to the minimum left position
    Then the text indicator should display the minimum value of "7"

  Scenario Outline: Saving dynamically selected habit durations
    When the user adjusts the duration slider to "<target_days>" days
    Then the habit duration should be successfully updated to "<target_days>" days

    Examples:
      | target_days |
      | 49          |
      | 25          |
      | 10          |
