Feature: About Us page Vision Card buttons after sign-in

  As a signed-in user
  I want to click the buttons on the Vision Cards
  So that I can navigate to the corresponding pages

  Background:
    Given the user is on the main page
    And the user is logged in with valid credentials


  Scenario: Verify Vision Card buttons after

  Scenario: Verify Vision Card buttons after sign-in
    When the user navigates to About Us page
    Then the About Us page should be opened

    When the user clicks Vision Card button 1
    Then the Places page should be opened
    And the user navigates back to About Us page


  Scenario: Verify Vision Card buttons after sign-in
    When the user navigates to About Us page
    Then the About Us page should be opened

    When the user clicks Vision Card button 1
    Then the Places page should be opened
    And the user navigates back to About Us page


  Scenario: Verify Vision Card buttons after sign-in
    When the user navigates to About Us page
    Then the About Us page should be opened

    When the user clicks Vision Card button 1
    Then the Places page should be opened
    And the user navigates back to About Us page
 sign-in
    When the user navigates to About Us page
    Then the About Us page should be opened

    When the user clicks Vision Card button 1
    Then the Places page should be opened
    And the user navigates back to About Us page

    When the user clicks Vision Card button 2
    Then the Friends page should be opened
    And the user navigates back to About Us page

    When the user clicks Vision Card button 3
    Then the Eco News page should be opened
    And the user navigates back to About Us page

    When the user clicks Vision Card button 4
    Then the Friends page should be opened
