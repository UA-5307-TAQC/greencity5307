Feature: Get social network image by URL

  As a client of the Social Network API
  I want to retrieve an image using its URL
  So that the image can be displayed in the application

  Background:
    Given the environment variable "BASE_API_URL" is configured
    And SocialNetworkClient is created using Config.BASE_API_URL

  Scenario Outline: Get social network image
    When I send a GET request to "/image" with image "<image_url>"
    Then the response status code should be captured

    Examples:
      | image_url                   |
      | https://picsum.photos/200   |

  Scenario: Successfully retrieve social network image
    Given a valid image URL
    When I send a GET request to "/image" with image "<image_url>"
    And the response status code is 200
    Then the response body should match "one_news_get_by_id_schema"

  Scenario: User has no permission to access the image
    Given a valid image URL
    When I send a GET request to "/image" with image "<image_url>"
    And the response status code is 400
    Then the response body should contain message "Current user has no permission for this action"

  Scenario: Image page not found
    Given an invalid image URL
    When I send a GET request to "/image" with image "<image_url>"
    And the response status code is 404
    Then the response body should contain message "Page is not found"

  Scenario: Forbidden access
    Given a request without proper authorization
    When I send a GET request to "/image" with image "<image_url>"
    And the response status code is 403
    Then the response body should contain message "Forbidden access"

  Scenario: Internal server error
    Given the server encounters an unexpected condition
    When I send a GET request to "/image" with image "<image_url>"
    And the response status code is 500
    Then the response body should contain message "Internal Server Error"

  Scenario: Unexpected status code
    When I send a GET request to "/image" with image "<image_url>"
    And the response status code is not one of [200, 400, 403, 404, 500]
    Then the test should fail with message "Other error"
