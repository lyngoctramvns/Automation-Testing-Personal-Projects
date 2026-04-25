Feature: Home Page
    Scenario: Verify the home page title
        Given I am on the home page
        When I check for page title
        Then I should see the title