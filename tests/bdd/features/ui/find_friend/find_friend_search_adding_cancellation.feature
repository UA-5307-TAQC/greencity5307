Feature: Find Friend Functionality

  # TC-FF-01
  Scenario Outline: User can send, persist, and cancel a friend request
    Given a target user with "<friend_id>" has no friend request
    And the user is signed in
    And the user is on the "Find Friend" page

    When the user searches for "<target_user>"
    And clicks the "Add Friend" button on the user card
    Then the notification "Friend request sent" should appear
    And the button on the user card should change to "Cancel request"

    When the user refreshes the "Find a friend" page
    And searches for "<target_user>" again
    Then the button on the user card should still be "Cancel request"

    When the user opens the profile of "<target_user>"
    Then the button on the profile page should be "Cancel request"

    When the user clicks the "Cancel request" button on the profile page
    Then the notification "Your friend request has been canceled" should appear
    And the button on the profile page should change to "Add friend"

    When the user navigates back to the "Find Friend" page
    And searches for "<target_user>" again
    Then the button on the user card should be "Add friend"
    Examples:
      | target_user       | friend_id |
      | Liubomyr Halamaha |    31     |
