Feature: Find Friend Functionality

  # TC-FF-01
  Scenario: User can send, persist, and cancel a friend request
    Given the user is logged in to GreenCity
    And a target user "Liubomyr Halamaha" is not in the user's friend list
    And the user is on the "Find Friend" page

    When the user searches for "Liubomyr Halamaha"
    And clicks the "Add Friend" button on the user card
    Then the button on the user card should change to "Cancel request"
    And the notification "Friend request sent" should appear

    When the user refreshes the page
    And searches for "Liubomyr Halamaha" again
    Then the button on the user card should still be "Cancel request"

    When the user opens the profile of "Liubomyr Halamaha"
    Then the button on the profile page should be "Cancel request"

    When the user clicks the "Cancel request" button on the profile page
    Then the notification "Your friend request has been canceled" should appear
    And the button on the profile page should change to "Add friend"

    When the user navigates back to the "Find Friend" page
    And searches for "Liubomyr Halamaha" again
    Then the button on the user card should be "Add friend"
