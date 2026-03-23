Feature: Like news on the one news page

  As a registered user
  I want to like or unlike a news article
  So that the like counter updates correctly

  Background:
    Given the user is signed in
    And the user is on the "My Space" page
    And the header navigation menu is visible

  Scenario: User likes or unlikes a news article from the one news page
    When the user navigates to the Eco News page
    And the user opens a random news article
    Then the user sees the current number of likes
    When the user clicks the like button
    Then the like counter should update accordingly
    And if the article was previously liked the counter decreases by 1
    And if the article was not previously liked the counter increases by 1
