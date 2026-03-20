Feature: Update habit duration

  Background:
    Given the user is logged in
    And the user is on the "My Habits" page

  Scenario Outline: User updates habit duration
    When the user edits the habit "<habit_name>"
    And changes the duration to "<duration>" days
    And clicks the "Save" button
    Then a success notification appears
    And the habit "<habit_name>" displays duration "<duration>" days

    Examples:
      | habit_name | duration |
      | Save Water | 14       |
      | Recycle    | 21       |
