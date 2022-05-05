Feature: User successfully logs into vsmonitor.com
  Scenario: User logs into the website with valid parameters
    Given Launch chrome browser
    When Opens VistaSoft Monitor login page
    And Enters e-mail "dd_test_1@outlook.com" and password "}krK,gdC6"
    And Clicks "Log-in" button
    Then User is successfully logged in
