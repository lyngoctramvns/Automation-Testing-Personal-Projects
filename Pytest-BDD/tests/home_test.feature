Feature: Home Page

    Scenario: Verify the home page title
        Given I am on the home page
        When I check for page title
        Then I should see the title

    Scenario: The booking section scrolled when Booking button is clicked
        Given I am on the home page
        When I click Booking button
        Then The site is scrolled to the booking section