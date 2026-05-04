
class Booking:
    def check_booking_form_visible(self, browser):
        booking_form = browser.find_by_xpath("//div[@class='card shadow booking-card']")
        return booking_form.visible

    def get_booking_form_title(self, browser):
        booking_form_title = browser.find_by_xpath("//h3[@class='card-title text-center mb-4']")
        return booking_form_title.text

    def booking_form_date_range_input(self, browser):
        