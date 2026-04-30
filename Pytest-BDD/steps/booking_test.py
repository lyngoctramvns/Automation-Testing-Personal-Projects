from pytest_bdd import scenario, given, when, then
import time

from src.Booking_class import Booking

new_booking = Booking()

# Booking form testing partitions: Form visibility, Title (confirm visibility & correctness), Date range field (end date, start date input, invalid range), Check Availability button (confirm visibility, confirm clickability, confirm correct response to click)

@scenario('../tests/home_test.feature', 'Verify the booking form is visible')
def booking_form_visible():
    pass

