Feature: Saved Abstract page tabs navigation

  As a signed-in user
  I want to navigate through tabs on the Saved page
  So that I can view saved Events, Places, and Eco-news

  Background:
    Given the user is on the main page
    And the user is logged in with valid credentials


  Scenario: Navigate through Events, Places, and Eco-news tabs
    When the user navigates to the Saved page
    Then the Saved page should be opened

    When the user goes to the "Events" tab
    Then the "Events" tab should be active

    When the user goes to the "Places" tab
    Then the "Places" tab should be active

    When the user goes to the "Eco-news" tab
    Then the "Eco-news" tab should be active
