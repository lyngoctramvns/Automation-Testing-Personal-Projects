
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

    def enter_date_range(self, browser, faker, date_range):
        if date_range == "future":
            check_in_date = faker.date_future().strftime("%Y-%m-%d")
            check_out_date = faker.date_future().strftime("%Y-%m-%d")
        else:
            check_in_date = faker.date_past().strftime("%Y-%m-%d")
            check_out_date = faker.date_future().strftime("%Y-%m-%d")
        browser.find_by_xpath("//label[contains(text(), 'Check In')]/following-sibling::div//input").fill(check_in_date)
        browser.find_by_xpath("//label[contains(text(), 'Check Out')]/following-sibling::div//input").fill(check_out_date)
        return check_in_date, check_out_date

    def click_check_availability_button(self, browser):
        availability_button = browser.find_by_xpath("//button[contains(text(), 'Check Availability')]")
        availability_button.click()

    def check_availability_result(self, browser):
        