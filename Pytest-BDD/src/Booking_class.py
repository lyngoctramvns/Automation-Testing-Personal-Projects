class Booking:
    def check_booking_form_visible(self, browser):
        booking_form = browser.find_element_by_xpath("//div[@class='card shadow booking-card']")
        return booking_form.is_displayed()