from faker import Faker
import time
import e2e.locators.booking

fake = Faker()

class Booking:
    def check_booking_form_visible(self, browser):
        booking_form = browser.find_by_xpath(e2e.locators.booking.booking_form)
        return booking_form.visible

    def get_booking_form_title(self, browser):
        booking_form_title = browser.find_by_xpath(e2e.locators.booking.booking_form_title)
        return booking_form_title.text

    def booking_form_date_range_input(self, browser):
        booking_form_check_in_input = browser.find_by_xpath(e2e.locators.booking.check_in_date_input)
        booking_form_check_out_input = browser.find_by_xpath(e2e.locators.booking.check_out_date_input)
        return booking_form_check_in_input.visible and booking_form_check_out_input.visible

    def enter_date_range(self, browser, date_range):
        if date_range == "future":
            check_in_date = fake.date_between(start_date="+0d", end_date="+1w").strftime("%d/%m/%Y")
            check_out_date = fake.date_between(start_date="+0d", end_date="+1w").strftime("%d/%m/%Y")
        elif date_range == "past":
            check_in_date = fake.date_between(start_date="-1m", end_date="-1d").strftime("%d/%m/%Y")
            check_out_date = fake.date_between(start_date="-1m", end_date="-1d").strftime("%d/%m/%Y")

        start_xpath = e2e.locators.booking.check_in_date_input
        end_xpath = e2e.locators.booking.check_out_date_input
        # clear elements fields, then fill them with the new values
        check_in_field = browser.find_by_xpath(start_xpath).first
        check_in_field.fill("")
        time.sleep(5)
        check_in_field.fill(check_in_date)
        check_out_field = browser.find_by_xpath(end_xpath).first
        check_out_field.fill("")
        time.sleep(5)
        check_out_field.fill(check_out_date)
        return check_in_date, check_out_date

    def click_check_availability_button(self, browser):
        availability_button = browser.find_by_xpath(e2e.locators.booking.check_availability_button)
        availability_button.click()

    def check_availability_rooms(self, browser):
        available_rooms = browser.find_by_xpath(e2e.locators.booking.rooms_available)
        return available_rooms.visible
        