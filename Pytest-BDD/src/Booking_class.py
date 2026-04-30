class Booking:
    def check_booking_form_visible(self, test_browser):
        booking_form = test_browser.find_element_by_id("booking-form")
        return booking_form.is_displayed()