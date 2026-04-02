Feature: Social Network Image

  As a user
  I want to retrieve social network images
  So that I can validate access and responses

  Scenario Outline: Get social network image with valid URL
    Given the user is authorized
    And I have SocialNetworkClient
    When I send GET request to social network image with url "<image_url>"
    Then the response status code should be <status_code>
    And the response should match social network image schema

  Examples:
    | image_url                  | status_code |
    | https://picsum.photos/200 | 200         |


  Scenario Outline: Get social network image with invalid URL
    Given the user is authorized
    And I have SocialNetworkClient
    When I send GET request to social network image with url "<image_url>"
    Then the response status code should be <status_code>
    And the response should contain "<message_type>" with value "<message>"

  Examples:
    | image_url                  | status_code | message_type | message                                             |
    | https://picsum.photos/400 | 400         | message      | Current user has no permission for this action      |
    | https://picsum.photos/404 | 404         | message      | Page is not found                                  |
    | https://picsum.photos/403 | 403         | error        | Forbidden                                          |
    | https://picsum.photos/500 | 500         | error        | Internal Server Error                              |
