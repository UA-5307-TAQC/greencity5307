Feature: Retrieve eco news

  Scenario Outline: API returns an error when invalid query parameters are used
    Given Get EcoNewsClient
    When the client sends a request to retrieve eco news with parameters
      | page   | size   | sort   |
      | <page> | <size> | <sort> |
    Then the response status code should be <status_code>
    And the response message should be <message>

    Examples:
      | page | size | sort                         | message                                                                                             | status_code |
      | -1   | 20   | null                         | page must be a positive number                                                                      | 400         |
      | 0    | -1   | null                         | size must be a positive number                                                                      | 400         |
      | 0    | 0    | null                         | Page size must be greater than or equal to 1                                                        | 400         |
      | 0    | 101  | null                         | Page size must be less than or equal to 100                                                         | 400         |
      | 0    | 20   | [not-created]                | Unsupported value for sorting: [not-created]                                                        | 400         |
      | 0    | 20   | [not-created, not-created-2] | Invalid value 'not-created-2' for orders given; Has to be either 'desc' or 'asc' (case insensitive) | 400         |


  Scenario Outline: API returns eco news list with valid filters
    Given Get EcoNewsClient
    When the client sends a request to retrieve eco news with parameters
      | page   | size   | tags   | title   | author_id   | favorite   |
      | <page> | <size> | <tags> | <title> | <author_id> | <favorite> |
    Then the response status code should be 200
    And the response should match schema page

    Examples:
      | page | size | tags              | title     | author_id | favorite |
      | 0    | 20   | null              | null      | null      | false    |
      | 10   | 12   | [news, education] | null      | null      | false    |
      | 0    | 30   | null              | Test      | null      | false    |
      | 0    | 100  | null              | null      | 1         | false    |
      | 100  | 100  | null              | null      | null      | false    |
      | 0    | 20   | null              | null      | 1         | true     |
      | 0    | 20   | null              | Test      | 1         | false    |
      | 0    | 20   | null              | Test      | 1         | true     |
      | 0    | 20   | [events]          | Test      | 1         | false    |
      | 0    | 20   | null              | null      | 1000000   | false    |
      | 0    | 20   | [not-exist]       | null      | 1000000   | false    |
      | 0    | 20   | null              | Not-exist | 1000000   | false    |
