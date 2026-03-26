Feature: Update Eco News

  Scenario Outline: Update eco news with valid data
    Given I am an authorized user
    When I send PUT request to update eco news with id "<news_id>" and payload:
      """
      <data>
      """
    Then the response status code should 200
    And the response should match schema eco_news

    Examples:
      | news_id | data |
      | 32 | {"id":"32","source":"https://example.org","shortInfo":"Climate change update","tags":["news","events"],"title":"Climate change update","content":"Full article text here","titleTranslation":{"content":"Climate News","languageCode":"en"},"textTranslation":{"content":"Full article text here","languageCode":"en"}} |
      | 45 | {"id":"45","source":"https://example.com","shortInfo":"New eco-friendly product launch","tags":["education","ads"],"title":"New eco-friendly product launch","content":"Full article text here","titleTranslation":{"content":"Eco Product Launch","languageCode":"en"},"textTranslation":{"content":"Details about the new product","languageCode":"en"}} |
      | 78 | {"id":"78","source":"https://example.net","shortInfo":"Upcoming environmental event","tags":["events"],"title":"Upcoming environmental event","content":"Full article text here","titleTranslation":{"content":"Environmental Event","languageCode":"en"},"textTranslation":{"content":"Event details and registration info","languageCode":"en"}} |


  Scenario Outline: Update eco news with invalid data
    Given I am an authorized user
    When I send PUT request to update eco news with id "<news_id>" and "<data>":
    Then the response status code should <status_code>
    And the response message should be "<message>"

    Examples:
      | news_id | data | status_code | message |
      | 32 | {"id":"32","source":"https://example.org","shortInfo":"Climate change update","tags":["not","not"],"title":"Climate change update","content":"Full article text here","titleTranslation":{"content":"Climate News","languageCode":"not"},"textTranslation":{"content":"Full article text here","languageCode":"not"}} | 400 | Current user has no permission for this action |
      | 78 | {"id":"78","source":"source","shortInfo":"Upcoming environmental event","tags":["events"],"title":"Upcoming environmental event","content":"Full article text here","titleTranslation":{"content":"Environmental Event","languageCode":"en"},"textTranslation":{"content":"Event details and registration info","languageCode":"en"}} | 404 | Eco new doesn't exist by this id: 78 |
