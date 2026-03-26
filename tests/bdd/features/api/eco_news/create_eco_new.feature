Feature: Create Eco News

  As an authenticated user
  I want to create eco news
  So that I can publish new articles

  Scenario Outline: Create eco news with valid data
    Given Get Create Eco News client
    When I send POST request to create eco news with data:
    """
    <data>
    """
    Then the response status code should be 201


  Examples:
    | data |
    | {"source":"https://example.org","shortInfo":"Climate change update","tags":["news","events"],"title":"Climate change update","text":"Full article text here","titleTranslation":{"content":"Climate News","languageCode":"en"},"textTranslation":{"content":"Full article text here","languageCode":"en"}} |
    | {"source":"https://example.com","shortInfo":"New eco-friendly product launch","tags":["education","ads"],"title":"New eco-friendly product launch","text":"Full article text here","titleTranslation":{"content":"Eco Product Launch","languageCode":"en"},"textTranslation":{"content":"Details about the new product","languageCode":"en"}} |
    | {"source":"https://example.net","shortInfo":"Upcoming environmental event","tags":["events"],"title":"Upcoming environmental event","text":"Full article text here","titleTranslation":{"content":"Environmental Event","languageCode":"en"},"textTranslation":{"content":"Event details and registration info","languageCode":"en"}} |
