Feature: Website language switching

  Background:
    Given the user opens the website
    And the homepage loads successfully

  Scenario Outline: User switches website language
    Given the current website language is "<current_language>"
    When the user opens the language switcher
    And selects "<new_language>"
    Then the page reloads
    And the navigation menu displays "<menu_text>"

    Examples:
      | current_language | new_language | menu_text   |
      | UA               | EN           | Eco News    |
      | EN               | UA           | Еко Новини  |
