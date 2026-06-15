import e2e.locators.rooms

class Rooms:
    def room_section(self, browser):
        room_section = browser.find_by_xpath(e2e.locators.rooms.section_rooms)
        return room_section
    def find_room_card(self, browser, room_name):
        room_card  = browser.find_by_xpath(e2e.locators.rooms.room_card.format(room_name=room_name))
        return room_card
    def booking_button(self, browser, booking_button, room_name):
        booking_button = browser.find_by_xpath(e2e.locators.rooms.room_booking_button.format(booking_button=booking_button, room_name=room_name))
        return booking_button
