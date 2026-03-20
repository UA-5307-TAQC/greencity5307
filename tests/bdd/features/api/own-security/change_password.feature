@API @security @HighPriority
Feature: API User Password Update Validation
  As an authenticated user of GreenCity
  I want to securely update my current password via the change-password API
  So that I can maintain the security of my account

  @HappyPath
  Scenario Outline: Successful password update with valid and matching inputs
    Given the user is authenticated and has a valid access token
    When a PUT request is sent to the "/ownSecurity/changePassword" endpoint with
      | password    | confirm_password   |
      | <password>  | <confirm_password> |
    Then the API should respond with a 200 OK status code
    And the response body should be an empty JSON or string

    Examples:
      | password           | confirm_password   |
      | NewstrongPassword1 | NewstrongPassword1 |


  # --- NEGATIVE SCENARIOS ---

  @Negative @Validation
  Scenario Outline: Unsuccessful password update due to validation errors
    Given the user is authenticated and has a valid access token
    When a PUT request is sent to the "/ownSecurity/changePassword" endpoint with
      | password   | confirmPassword    |
      | <password> | <confirm_password> |
    Then the API should respond with a <status_code> Bad Request status code
    And the response error message should contain "<error_message>"

    Examples:
      | password            | confirm_password    | status_code | error_message                                     |
      | StrongPass1!        | DifferentPass2@     | 400         | The passwords don't match                       |
      | StrongPass1!        |                     | 400         | must not be blank                                 |
      | 123                 | 123                 | 400         | password must be 8 or more characters in length   |

  @Negative @Security @Unauthorized
  Scenario: Unsuccessful password update attempt without authentication
    Given the user is NOT authenticated (does not have a valid access token)
    When a PUT request is sent to the "/ownSecurity/changePassword" endpoint with
      | password        | StrongPass1! |
      | confirmPassword | StrongPass1! |
    Then the API should respond with a 401 Unauthorized status code
    And the response error message should contain "Unauthorized"
