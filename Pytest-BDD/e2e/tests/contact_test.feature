Feature: Contact Form at Home Page
    Scenario: Verify the contact form is visible
        Given I am on the home page
        Then The contact form should be visible

    Scenario: Verify the contact form title is visible
        Given I am on the home page
        Then The contact form title should be visible

    Scenario Outline: Verify the name, email, phone, subject, and message fields are visible
        Given I am on the home page
        Then The "<field>" field should be visible
        Examples:
            | field   |
            | Name    |
            | Email   |
            | Phone   |
            | Subject |
            | Message |

    Scenario Outline: Should see corresponding result when submit contact form
        Given I am on the home page
        When I fill in the contact form with "<Name>", "<Email>", "<Phone>", "<Subject>", and "<Message>"
        And I submit the contact form
        Then I should see a "<Status>" message
        Examples:
        | Name | Email | Phone | Subject | Message | Status |
        | John Doe | john.doe@example.com | 07123456789 | Inquiry About Service | Hello, I would like to know more about your services. | Success |
        | John Doe | john.doe@example.com | 123 | Inquiry About Service | Hello, I would like to know more about your services. | Error - Invalid Phone Number |
        | John Doe | wrong email | 07123456789 | Inquiry About Service | Hello, I would like to know more about your services. | Error - Invalid Email |
        | John Doe | john.doe@example.com | 07123456789 | s | Hello, I would like to know more about your services. | Error - Invalid Subject |
        | John Doe | john.doe@example.com | 07123456789 | Inquiry About Service | short | Error - Invalid Message |
