Feature: Update user

  Scenario Outline: Update user with valid and invalid data
    Given the user is authorized
    And created UserClient
    When I send request to update user with payload: <payload>
    Then response status code should be <status>

    Examples:
      | payload                                                                   | status |
      | {"name":"Іван Петренко","emailNotification":"IMMEDIATELY"}                | 200    |
      | {"name":"John Doe","emailNotification":"DAILY"}                           | 200    |
      | {"name":"Марія-Анна","emailNotification":"WEEKLY"}                        | 200    |
      | {"name":"Ivan O'Connor","emailNotification":"MONTHLY"}                    | 200    |

      | {"name":"Іван..Петро","emailNotification":"IMMEDIATELY"}                  | 400    |
      | {"name":"Іван.","emailNotification":"IMMEDIATELY"}                        | 400    |
      | {"name":"Іван--Петро","emailNotification":"DAILY"}                        | 400    |
      | {"name":"Ivan@Petro!","emailNotification":"WEEKLY"}                       | 400    |
      | {"name":"IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII","emailNotification":"MONTHLY"} | 400    |
      | {"name":"Іван","emailNotification":"YEARLY"}                              | 400    |
      | {"name":"Іван Петренко","emailNotification":""}                           | 400    |

  Scenario Outline: Update user without valid access token
    Given I have invalid access token
    And created UserClient
    When I send request to update user with payload: <payload>
    Then validate if unauthorised

    Examples:
      | payload                                                    |
      | {"name":"Іван Петренко","emailNotification":"IMMEDIATELY"} |
      | {"name":"John Doe","emailNotification":"DAILY"}            |
