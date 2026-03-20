Feature: Like news on the one news page

  As a registered user
  I want to like or unlike a news article
  So that the like counter updates correctly

  Scenario: User likes or unlikes a news article from the one news page
    Given the user opens the main page
    And the user signs in with valid credentials
    When the user navigates to the Eco News page
    And the user opens a random news article
    Then the user sees the current number of likes
    When the user clicks the like button
    Then the like counter should update accordingly
    And if the article was previously liked the counter decreases by 1
    And if the article was not previously liked the counter increases by 1
