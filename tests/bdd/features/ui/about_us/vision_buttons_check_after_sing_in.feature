Feature: About Us page Vision Card buttons before sign-in

  As a user who is not signed in
  I want to click the buttons on the Vision Cards
  So that I can see either the sign-in modal or navigate to News page


  Scenario: Verify Vision Card buttons without sign-in
    When the user navigates to About Us page
    Then the About Us page should be opened

    When the user clicks Vision Card button 1 without signing in
    Then the Sign In modal should be displayed
    And the user closes the Sign In modal
    Then the Main page should be opened
    And the user navigates back to About Us page

    When the user clicks Vision Card button 2 without signing in
    Then the Sign In modal should be displayed
    And the user closes the Sign In modal
    Then the Main page should be opened
    And the user navigates back to About Us page

    When the user clicks Vision Card button 3 without signing in
    Then the Eco News page should be opened
    And the user navigates back to About Us page

    When the user clicks Vision Card button 4 without signing in
    Then the Sign In modal should be displayed
    And the user closes the Sign In modal
    Then the Main page should be opened
    And the user navigates back to About Us page
