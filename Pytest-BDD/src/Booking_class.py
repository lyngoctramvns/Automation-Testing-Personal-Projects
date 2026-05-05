
class Booking:
    def check_booking_form_visible(self, browser):
        booking_form = browser.find_by_xpath("//div[@class='card shadow booking-card']")
        return booking_form.visible

    def get_booking_form_title(self, browser):
        booking_form_title = browser.find_by_xpath("//h3[@class='card-title text-center mb-4']")
        return booking_form_title.text

    def booking_form_date_range_input(self, browser):
        booking_form_check_in_input = browser.find_by_xpath("//label[contains(text(), 'Check In')]/following-sibling::div//input")
        booking_form_check_out_input = browser.find_by_xpath("//label[contains(text(), 'Check Out')]/following-sibling::div//input")
        return booking_form_check_in_input.visible and booking_form_check_out_input.visible