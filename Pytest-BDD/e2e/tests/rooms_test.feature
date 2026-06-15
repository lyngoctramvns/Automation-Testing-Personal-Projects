Feature: Rooms
    Scenario: The rooms should be visible under booking form section
        Given I am on the home page
        Then I should see the rooms section under booking form section

    Scenario Outline: Rooms should be displayed by default
        Given I am on the home page
        Then I should see the <room> displayed by default
        Examples:
            | room   |
            | Single |
            | Double |
            | Suite  |

    Scenario Outline: The Book Now button should redirect to the booking page
        Given I am on the home page
        And The "Book now" button is visible under each <room>
        When I click on the "Book now" button under each <room>
        Then I should be redirected to the booking page
        Examples:
            | room   |
            | Single |
            | Double |
            | Suite  |
      