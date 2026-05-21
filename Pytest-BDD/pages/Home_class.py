import os
from dotenv import load_dotenv, dotenv_values
import locators.home

load_dotenv()

class Home: 
    def visit_page(self, browser):
        browser.visit(os.getenv("SITE_URL"))

    def get_title(self, browser):
        get_page_title = browser.find_by_xpath(locators.home.title).text
        return get_page_title
    
    def click_booking_button(self, browser):
        browser.find_by_xpath(locators.home.booking_button).click()
    
    def is_booking_section_visible(self, browser):
        # Check if booking section element is visible
        booking_section = browser.find_by_xpath(locators.home.booking_section)
        return booking_section.visible

    

