import e2e.locators.contact
class Contact:
    def contact_form(self, browser):
        contact_form = browser.find_by_xpath(e2e.locators.contact.contact_form)
        return contact_form
    def contact_title(self, browser):
        contact_title = browser.find_by_xpath(e2e.locators.contact.contact_title.format(contact_form=e2e.locators.contact.contact_form))
        return contact_title
    def contact_field(self, browser, field):
        if field == "Message":
            locator = e2e.locators.contact.contact_message_field
        else:
            locator = e2e.locators.contact.contact_field
        contact_field = browser.find_by_xpath(locator.format(contact_form=e2e.locators.contact.contact_form, field=field))
        return contact_field
    def contact_field_fill(self, browser, field_name, value):
        contact_field_locator = self.contact_field(browser, field_name)
        contact_field_locator.fill(value)
    def contact_form_submit(self, browser):
        submit_button = browser.find_by_xpath(
            e2e.locators.contact.contact_button.format(contact_form=e2e.locators.contact.contact_form)
        )
        browser.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
            submit_button._element,
        )
        try:
            submit_button.click()
        except Exception: #fall back to JS click if normal click fails
            browser.driver.execute_script("arguments[0].click();", submit_button._element)
        return submit_button
    def contact_form_message(self, browser, status):
        success_message = browser.find_by_xpath(e2e.locators.contact.success_div.format(contact_form=e2e.locators.contact.contact_form))
        error_message = browser.find_by_xpath(e2e.locators.contact.error_div)
        match status:
            case "Success":
                assert "Thanks for getting in touch" in success_message.text
            case "Error - Invalid Email":
                assert "must be a well-formed email address" in error_message.text
            case "Error - Invalid Phone Number":
                assert "Phone must be between 11 and 21 characters." in error_message.text
            case "Error - Invalid Subject":
                assert "Subject must be between 5 and 100 characters." in error_message.text
            case "Error - Invalid Message":
                assert "Message must be between 20 and 2000 characters." in error_message.text