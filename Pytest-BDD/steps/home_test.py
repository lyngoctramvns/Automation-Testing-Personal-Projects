from pytest_bdd import scenario, given, when, then
import time

from src.Home_class import Home

new_home = Home()

@scenario('../tests/home_test.feature', 'Verify the home page title')
def test_home_page_title():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@when('I check for page title')
def check_for_page_title():
    pass

@then('I should see the title')
def check_page_title(test_browser):
    check_page_title = new_home.get_title(test_browser)
    assert "Shady Meadows B&B" in check_page_title

@scenario('../tests/home_test.feature', 'The booking section scrolled when Booking button is clicked')
def test_booking_section_scrolled():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@when('I click Booking button')
def click_booking_button(test_browser):
    new_home.click_booking_button(test_browser)

@then('The site is scrolled to the booking section')
def check_scrolled_to_booking(test_browser):
    time.sleep(1)
    # Check if booking section is visible
    assert new_home.is_booking_section_visible(test_browser), "Booking section is not visible after clicking booking button"


