Feature: Social Network Deletion

  As a user
  I want to verify access restrictions for deleting social networks
  So that unauthorized actions are prevented

  Scenario Outline: Try to delete social network without permission
    Given the user is authorized
    And I have SocialNetworkClient
    When I send DELETE request to social network with id "<network_id>"
    Then the response status code should be <status_code>
    And the response should match social network schema if status is 403
    And the response should contain "<message_type>" with value "<message>"

  Examples:
    | network_id | status_code | message   | message_type |
    | 1          | 403         | Forbidden | error        |
    | 32         | 403         | Forbidden | error        |
    | 2          | 403         | Forbidden | error        |
    | 77         | 403         | Forbidden | error        |
    | 90         | 403         | Forbidden | error        |
