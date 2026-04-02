Feature: User Registration and Verification
  As a new user
  I want to register an account and verify my email
  So that I can securely access the system
@security_api
  Scenario: Successful Sign Up and Email Verification
    Given a new user with a unique email address
    When register the user via the security API
    Then should receive a verification email via Mailosaur
    And navigate to the verification link
    And should be able to sign in and receive an access token
