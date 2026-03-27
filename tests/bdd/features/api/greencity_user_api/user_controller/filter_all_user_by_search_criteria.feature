Feature: Filter all users by search criteria

  Scenario Outline: Filter users with valid parameters
    Given the user is authorized
    Given created UserClient
    When I send request to filter user by page with filters: <query> and <json>
    Then validate schema for filter user by page with filters if successful
    And validate if user access is forbidden
    And user response status code should be successful or forbidden

    Examples:
      | query                     | json                  |
      | {}                        | {"searchReg": ""}     |
      | {"page": 0, "size": 5}    | {"searchReg": "test"} |
      | {"page": 1, "size": 10}   | {"searchReg": "john"} |
      | {"page": 0, "size": 1}    | {"searchReg": ""}     |
      | {"page": 10, "size": 100} | {"searchReg": "abc"}  |

  Scenario Outline: Filter users without access token
    Given I have invalid access token
    Given created UserClient
    When I send request to filter user by page with filters: <query> and <json>
    Then validate if unauthorised

    Examples:
      | query                     | json                  |
      | {}                        | {"searchReg": ""}     |
      | {"page": 0, "size": 5}    | {"searchReg": "test"} |
      | {"page": 1, "size": 10}   | {"searchReg": "john"} |
      | {"page": 0, "size": 1}    | {"searchReg": ""}     |
      | {"page": 10, "size": 100} | {"searchReg": "abc"}  |

  Scenario Outline: Filter users with invalid parameters
    Given the user is authorized
    Given created UserClient
    When I send request to filter user by page with filters: <query> and <json>
    Then validate if bad request

    Examples:
      | query                                | json                  |
      | {"page": -1, "size": 5}              | {"searchReg": ""}     |
      | {"page": null, "size": 5}            | {"searchReg": ""}     |
      | {"page": 0, "size": 0}               | {"searchReg": ""}     |
      | {"page": 0, "size": 101}             | {"searchReg": ""}     |
      | {"page": 2}                          | {"searchReg": "test"} |
      | {"size": 20}                         | {"searchReg": "test"} |
      | {"sort": "asc"}                      | {"searchReg": ""}     |
      | {"sort": "desc"}                     | {"searchReg": ""}     |
      | {"sort": "name"}                     | {"searchReg": ""}     |
      | {"sort": "name,asc&sort=email,desc"} | {"searchReg": ""}     |
      | {"page": "abc", "size": 5}           | {"searchReg": ""}     |
      | {"page": 0, "size": "big"}           | {"searchReg": ""}     |
      | {"sort": "wrong_format"}             | {"searchReg": ""}     |
