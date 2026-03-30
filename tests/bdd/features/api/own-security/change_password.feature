Feature: User Password Update API
  As a registered and authenticated user
  I want to be able to update my account password
  So that I can maintain my account security

  @positive @restore_password
  Scenario: Successful password update with valid and matching inputs
    Given the user is authenticated with a valid access token
    When the user sends a PUT request to change the password with "NewstrongPassword1!" and confirm password "NewstrongPassword1!"
    Then the response status code should be 200
    And the response time should be less than 3000 ms
    And the response body should be empty or "{}"
    # Примітка: Відновлення пароля (teardown) зазвичай ховається у hooks (наприклад, @after_scenario), а не пишеться у BDD кроках.

  @negative @validation
  Scenario Outline: Password update validation for invalid inputs: <scenario_name>
    Given the user is authenticated with a valid access token
    When the user sends a PUT request to change the password with new password "<new_password>" and confirm password "<confirm_password>"
    Then the response status code should be <expected_status>
    And the response matches the 400 Bad Request JSON schema
    And the response error message should contain "<expected_error_text>"

    Examples:
      | scenario_name          | new_password | confirm_password | expected_status | expected_error_text                      |
      | Mismatched passwords   | StrongPass1! | DifferentPass2@  | 400             | The passwords don't match                |
      | Empty confirm password | StrongPass1! | [empty]          | 400             | must not be blank                        |
      | Password too short     | 123          | 123              | 400             | password must be 8 or more characters in |

@negative @security
  Scenario: Unsuccessful password update attempt without authentication
    Given the user is unauthenticated (no access token provided)
    When the user sends a PUT request to change the password with new password "NewstrongPassword1!" and confirm password "NewstrongPassword1!"
    Then the response status code should be 401
    And the response matches the 401 Unauthorized JSON schema
    And the response error message should contain "unauthorized"
