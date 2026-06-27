from pytest_bdd import scenario, given, when, then, parsers
import time

from pages.Contact_class import Contact
from pages.Home_class import Home

new_contact = Contact()
new_home = Home()

@scenario('../tests/contact_test.feature', 'Verify the contact form is visible')
def test_contact_form_visible():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then('The contact form should be visible')
def verify_contact_form_visible(test_browser):
    contact_form = new_contact.contact_form(test_browser)
    assert contact_form.visible, "Contact form is not visible on the home page"

@scenario('../tests/contact_test.feature', 'Verify the contact form title is visible')
def test_contact_form_title_visible():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then('The contact form title should be visible')
def verify_contact_form_title_visible(test_browser):
    contact_title = new_contact.contact_title(test_browser)
    assert contact_title.visible, "Contact form title is not visible on the home page"

@scenario('../tests/contact_test.feature', 'Verify the name, email, phone, subject, and message fields are visible')
def test_fields_visible():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then(parsers.parse('The "{field}" field should be visible'))
def verify_field_visible(test_browser, field):
    contact_field = new_contact.contact_field(test_browser, field)
    assert contact_field.visible, f"{field} field is not visible on the home page"

@scenario('../tests/contact_test.feature', 'Should see corresponding result when submit contact form')
def test_submit_contact_form():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@when(parsers.parse('I fill in the contact form with "{Name}", "{Email}", "{Phone}", "{Subject}", and "{Message}"'))
def fill_contact_form(test_browser, Name, Email, Phone, Subject, Message):
    new_contact.contact_field_fill(test_browser, 'Name', Name)
    new_contact.contact_field_fill(test_browser, 'Email', Email)
    new_contact.contact_field_fill(test_browser, 'Phone', Phone)
    new_contact.contact_field_fill(test_browser, 'Subject', Subject)
    new_contact.contact_field_fill(test_browser, 'Message', Message)

@when('I submit the contact form')
def submit_contact_form(test_browser):
    new_contact.contact_form_submit(test_browser)

@then(parsers.parse('I should see a {Status} message'))
def verify_response(test_browser, Status):
    time.sleep(5)
    new_contact.contact_form_message(test_browser, Status)