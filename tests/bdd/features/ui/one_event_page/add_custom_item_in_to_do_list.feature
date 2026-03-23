@wip
Feature: Custom To-Do List Items in Habits
  As a GreenCity user
  I want to add custom items to my habit's To-Do list
  So that I can personalize my habit tracking and goals

  Background:
    Given the user is logged into GreenCity
    And the user is on the "My Habits" tab in "My Space"
    And the user has opened a specific habit
    And the user has scrolled down to the Habit info section where the To-Do list is visible

  Scenario: Successfully adding and saving a new custom item
    When the user clicks the Edit (pencil) icon next to the To-Do list
    Then the To-Do list should switch to edit mode
    And the "Add custom item" input field should appear

    When the user enters "Eco Bag" into the "Add custom item" field
    And the user clicks the "+" (Add) button
    Then the input field should be cleared
    And the new item "Eco Bag" should be displayed at the top of the list

    When the user clicks the Save button
    Then the edit mode should close
    And the "Eco Bag" item should be successfully saved and displayed in the To-Do list
