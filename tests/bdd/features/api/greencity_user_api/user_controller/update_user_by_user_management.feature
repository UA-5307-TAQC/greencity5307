Feature: Update user by UserManagement

  Scenario Outline: Update user with valid and invalid data
    Given the user is authorized
    And created UserClient
    When I send request to update user by user management with payload: <payload>
    Then response status code should be <status>

    Examples:
      | payload                                                                                        | status |
      | {"name":"Іван Петренко","email":"ivan@example.com","role":"ROLE_USER","userStatus":"VERIFIED"} | 200    |
      | {"name":"John-Doe","email":"john.doe@test.com","role":"ROLE_ADMIN","userStatus":"CREATED"}     | 200    |
      | {"name":"Марія","email":"maria@test.com","role":"ROLE_EMPLOYEE","userStatus":"VERIFIED"}       | 200    |

      | {"name":"Іван..Петро","email":"ivan@test.com","role":"ROLE_USER","userStatus":"VERIFIED"}      | 400    |
      | {"name":"Іван.","email":"ivan@test.com","role":"ROLE_USER","userStatus":"VERIFIED"}            | 400    |
      | {"name":"Іван","email":"ivan@test.com","role":"ROLE_SUPER_ADMIN","userStatus":"VERIFIED"}      | 400    |
      | {"name":"Іван","email":"ivan@test.com","role":"ROLE_USER","userStatus":"DELETED"}              | 400    |
      | {"name":"Іван","email":null,"role":"ROLE_USER","userStatus":"VERIFIED"}                        | 400    |

  Scenario Outline: Update user with invalid access token
    Given I have invalid access token
    And created UserClient
    When I send request to update user by user management with payload: <payload>
    Then validate if unauthorised

    Examples:
      | payload                                                                                        |
      | {"name":"Іван Петренко","email":"ivan@example.com","role":"ROLE_USER","userStatus":"VERIFIED"} |
      | {"name":"John-Doe","email":"john.doe@test.com","role":"ROLE_ADMIN","userStatus":"CREATED"}     |
