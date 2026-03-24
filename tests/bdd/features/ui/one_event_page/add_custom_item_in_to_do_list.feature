Feature: Custom To-Do List Items in Habits
  As a GreenCity user
  I want to add custom items to my habit's To-Do list
  So that I can personalize my habit tracking and goals

  Background:
    Given the user is successfully logged in
    And the user has opened a specific habit

  Scenario: Successfully adding a new custom item
    When the user adds a custom item "Eco Bag" to the To-Do list
    Then the "Eco Bag" item should be displayed in the To-Do list
