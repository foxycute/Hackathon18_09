Feature: Login user account

  Scenario: Login user account
    Given I have account
    When I open Login page
    And enter my email and password
    And press a button "Log in"
    Then I see main page