Feature: Create an Account

  Scenario: Register new user
    Given I open Login page
    When created new user
    Then I see welcome text
    And I see main banner
