@wip
@API @authentication @HighPriority
Feature: API User Sign-In Validation
As a registered user of GreenCity
I want to authenticate via the sign-in API
So that I can securely access my account and receive a valid access token

Scenario: Successful authentication with valid credentials
Given the user has valid credentials (email and password)
And the project name is set to "GREENCITY"
When a POST request is sent to the "/ownSecurity/signIn" endpoint with the credentials payload
Then the API should respond with a 200 OK status code
And the response body should contain a valid numeric "userId"
And the response body should contain the name "Oleksandr"
And the "ownRegistrations" flag in the response should be true
And the response should contain an "accessToken"
And the "accessToken" must be a valid, decodable JWT
And the "accessToken" must contain a future expiration timestamp ("exp")
