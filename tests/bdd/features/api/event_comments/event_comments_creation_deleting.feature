@wip
Feature: Event Comments API functionality

  # TC-AEC-01
  Scenario: Unauthorized user cannot leave a comment on an event
    Given the user is not authenticated
    When the user sends a POST request to add a comment to event 31
    Then the response status code should be 401

  # TC-AEC-02
  Scenario: Authorized user can successfully leave and delete a comment
    Given the user is authenticated
    And the user gets the initial comment count for event 31

    When the user sends a POST request to add a comment to event 31
    Then the response status code should be 201
    And the comment count for event 31 should be incremented by 1

    When the user sends a DELETE request to remove the created comment
    Then the response status code should be 200
    And the comment count for event 31 should be returned to the initial value
