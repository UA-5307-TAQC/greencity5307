Feature: Header navigation functionality

  Background:
    Given the user is successfully logged in
    And the user is on the "My Space" page
    And the header navigation menu is visible

  Scenario: User navigates to Eco News page
    When the user clicks on "Eco-news" in the header navigation
    Then the user is redirected to the Eco News page
    And the URL contains "/news"
    And the page title is "Eco news"

  Scenario: User navigates to Events page
    When the user clicks on "Events" in the header navigation
    Then the user is redirected to the Events page
    And the page content is loaded successfully

  Scenario: User navigates to Places / Map page
    When the user clicks on "Places" in the header navigation
    Then the user is redirected to the Map page
    And the map component is visible

  Scenario: User navigates to About Us page
    When the user clicks on "About us" in the header navigation
    Then the user is redirected to the About Us page
    And the project information is displayed

  Scenario: User navigates to Home page via GreenCity logo
    When the user clicks the "GreenCity" logo in the header
    Then the user is redirected to the Homepage
    And the landing page content is displayed
