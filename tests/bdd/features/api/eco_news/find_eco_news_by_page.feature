Feature: Retrieve eco news

  Scenario Outline: API returns an error when invalid query parameters are used
    Given the API client is configured with the base API URL
    When the client sends a request to retrieve eco news with
      | page | <page> |
      | size | <size> |
      | sort | <sort> |
    Then the response status code should be <status_code>
    And the response message should be "<message>"

    Examples:
      | page | size | sort                         | message                                                                                          | status_code |
      | -1   | 20   | None                         | page must be a positive number                                                                   | 400 |
      | 0    | -1   | None                         | size must be a positive number                                                                   | 400 |
      | 0    | 0    | None                         | Page size must be greater than or equal to 1                                                     | 400 |
      | 0    | 101  | None                         | Page size must be less than or equal to 100                                                      | 400 |
      | 0    | 20   | [not-created]                | Unsupported value for sorting: [not-created]                                                     | 400 |
      | 0    | 20   | [not-created, not-created-2] | Invalid value 'not-created-2' for orders given; Has to be either 'desc' or 'asc' (case insensitive) | 400 |


  Scenario Outline: API returns eco news list with valid filters
    Given the API client is configured with the base API URL
    When the client sends a request to retrieve eco news with
      | page      | <page> |
      | size      | <size> |
      | tags      | <tags> |
      | title     | <title> |
      | author_id | <author_id> |
      | favorite  | <favorite> |
    Then the response status code should be 200
    And the response body should match the eco news response schema

    Examples:
      | page | size | tags              | title       | author_id | favorite |
      | 0    | 20   | None              | None        | None      | False |
      | 10   | 12   | [news, education] | None        | None      | False |
      | 0    | 30   | None              | Test        | None      | False |
      | 0    | 100  | None              | None        | 1         | False |
      | 100  | 100  | None              | None        | None      | False |
      | 0    | 20   | None              | None        | 1         | True |
      | 0    | 20   | None              | Test        | 1         | False |
      | 0    | 20   | None              | Test        | 1         | True |
      | 0    | 20   | [events]          | Test        | 1         | False |
      | 0    | 20   | None              | None        | 1000000   | False |
      | 0    | 20   | [not-exist]       | None        | 1000000   | False |
      | 0    | 20   | None              | Not-exist   | 1000000   | False |
