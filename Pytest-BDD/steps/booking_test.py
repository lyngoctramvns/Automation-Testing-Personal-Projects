from pytest_bdd import scenario, given, when, then, parsers
import time

from src.Home_class import Home
from src.Booking_class import Booking

new_home = Home()
new_booking = Booking()

# Booking form testing partitions: Form visibility, Title (confirm visibility & correctness), Date range field (end date, start date input, invalid range), Check Availability button (confirm visibility, confirm clickability, confirm correct response to click)

@scenario('../tests/booking_test.feature', 'Verify the booking form is visible')
def test_booking_form_visible():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then('The booking form should be visible')
def check_booking_form_visible(test_browser):
    time.sleep(1)
    assert new_booking.check_booking_form_visible(test_browser), "Booking form is not visible on the home page"

@scenario('../tests/booking_test.feature', 'Verify the booking form title')
def test_booking_form_title():
    pass

@given('I am on the booking form page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then('The booking form title should be visible')
def check_booking_form_title(test_browser):
    assert new_booking.get_booking_form_title(test_browser), "Booking form title is not visible on the booking form page"

@scenario('../tests/booking_test.feature', 'Verify the booking form date range field is visible')
def test_booking_form_date_range_field_visible():
    pass

@given('The booking form is visible')
def check_booking_form_visible(test_browser):
    assert new_booking.check_booking_form_visible(test_browser), "Booking form is not visible on the home page"

@then('The booking form date range input fields should be visible')
def check_booking_form_date_range_input(test_browser):
    assert new_booking.booking_form_date_range_input(test_browser), "Booking form date range input fields are not visible on the booking form page"

@scenario('../tests/booking_test.feature', 'Enter valid date range and click Check Availability button')
def test_valid_date_time_input():
    pass

@given('The booking form is visible')
def check_booking_form_visible(test_browser):
    assert new_booking.check_booking_form_visible(test_browser), "Booking form is not visible on the home page"

@when(parsers.parse('I enter the "{date_range}" date range'))
def enter_valid_date_range(test_browser, date_range):
    new_booking.enter_date_range(test_browser, date_range)

@when('I click Check Availability button')
def click_check_availability_button(test_browser):
    new_booking.click_check_availability_button(test_browser)

@then('The availability result should be visible')
def check_availability_rooms(test_browser):