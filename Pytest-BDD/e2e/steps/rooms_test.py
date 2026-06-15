import time

from pytest_bdd import given, scenario, when, then, parsers

from pages.Home_class import Home
from pages.Booking_class import Booking
from pages.Rooms_class import Rooms
import e2e.locators.booking

new_home = Home()
new_booking = Booking()
new_room = Rooms()

@scenario('../tests/rooms_test.feature', 'The rooms should be visible under booking form section')
def test_rooms_section_visible():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then('I should see the rooms section under booking form section')
def check_rooms_section_visible(test_browser):
    room_section = new_room.room_section(test_browser)
    assert room_section.visible

@scenario('../tests/rooms_test.feature', 'Rooms should be displayed by default')
def test_rooms_displayed_by_default():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@then(parsers.parse('I should see the {room} displayed by default'))
def check_room_displayed_by_default(test_browser, room):
    room_card = new_room.find_room_card(test_browser, room)
    assert room_card.visible, f"{room} is not visible by default"

@scenario('../tests/rooms_test.feature', 'The Book Now button should redirect to the booking page')
def test_book_now_button_redirect():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    new_home.visit_page(test_browser)

@given(parsers.parse('The "{booking_button}" button is visible under each {room}'))
def check_book_now_button_visible(test_browser, booking_button, room):
    booking_button_element = new_room.booking_button(test_browser, booking_button, room)
    assert booking_button_element.visible, f"{booking_button} button is not visible under {room}"

@when(parsers.parse('I click on the "{booking_button}" button under each {room}'))
def click_book_now_button(test_browser, booking_button, room):
    booking_button_element = new_room.booking_button(test_browser, booking_button, room)
    href = booking_button_element['href']
    test_browser.visit(href)

@then('I should be redirected to the booking page')
def redirect_to_booking_page(test_browser):
    time.sleep(5)  # Wait for the page to load
    assert e2e.locators.booking.booking_page in test_browser.url