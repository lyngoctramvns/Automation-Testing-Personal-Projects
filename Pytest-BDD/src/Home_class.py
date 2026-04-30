

class Home: 
    def visit_page(self, browser):
        browser.visit("https://automationintesting.online/")

    def get_title(self, browser):
        get_page_title = browser.find_by_xpath("//div[@class='container']//a[@class='navbar-brand d-flex align-items-center']//span").text
        return get_page_title
    
    def click_booking_button(self, browser):
        browser.find_by_xpath("//a[@class='btn btn-primary btn-lg']").click()
    
    def is_booking_section_visible(self, browser):
        # Check if booking section element is visible
        booking_section = browser.find_by_xpath("//div[@class='card shadow booking-card']//div[@class='card-body p-4']")
        return booking_section.visible

    

