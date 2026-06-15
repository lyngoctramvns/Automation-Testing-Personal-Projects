section_rooms = "//section[@id='rooms']"
room_card = "//div[@class='card-body' and .//h5[text()='{room_name}']]"
room_booking_button = "//div[@class='card-body' and .//h5[text()='{room_name}']]/following-sibling::div[contains(@class, 'card-footer')]//a[text()='{booking_button}']"