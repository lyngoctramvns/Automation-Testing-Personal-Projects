Feature: Booking

    Scenario: Verify the booking form is visible
        Given I am on the home page
        Then The booking form should be visible

    Scenario: Verify the booking form title
        Given I am on the home page
        Then The booking form title should be visible

    Scenario: Verify the booking form date range field is visible
        Given The booking form is visible
        Then The booking form date range input fields should be visible

    Scenario: Enter valid date range and click Check Availability button
        Given The booking form is visible
        When I enter the valid date range
        And I click Check Availability button
        Then The availability result should be visible