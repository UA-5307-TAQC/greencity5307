@wip
Feature: Habit Duration Customization
  As a GreenCity user
  I want to adjust the duration of my habits using a slider
  So that I can set custom timelines for my goals

  Background:
    Given the user is logged into GreenCity
    And the user has at least one habit in "My Habits"
    And the user has opened a habit card
    And the user has scrolled to the "Duration" section
    And the duration slider is initially set to the default value of "7 d"

  Scenario: Dynamic text update while dragging the slider
    When the user clicks, holds, and drags the slider handle to the right
    Then the slider should move smoothly
    And the text indicator should update dynamically to reflect the current position, such as "25 d"

  Scenario: Slider stops at the maximum duration boundary
    When the user drags the slider handle to the maximum right position
    Then the slider should physically stop at the end of the bar
    And the text indicator should display the maximum value of "56 d"

  Scenario: Saving a newly selected habit duration
    Given the user has adjusted the duration slider to a new value, such as "56 d"
    When value rise "56 d"
    Then the newly selected duration should be display successfully
    And the habit duration should be updated to the selected value

  Scenario: Saving a minimum habit duration of 7 days
    Given the user has adjusted the duration slider to "7 d"
    When value rise "7 d"
    Then the newly selected duration should be display successfully
    And the habit duration should be updated to the selected value

  Scenario: Saving a specific habit duration of 10 days
    Given the user has adjusted the duration slider to "10 d"
    When value rise "10 d"
    Then the newly selected duration should be display successfully
    And the habit duration should be updated to the selected value
