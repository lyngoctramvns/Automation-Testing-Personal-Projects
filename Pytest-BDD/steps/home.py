from pytest_bdd import scenario, given, when, then

@scenario('../tests/home.feature', 'Verify the home page title')
def test_home_page_title():
    pass

@given('I am on the home page')
def go_to_home_page(test_browser):
    test_browser.visit("https://automationintesting.online/")

@when('I check for page title')
def check_for_page_title(test_browser):
    pass

@then('I should see the title')
def check_page_title(test_browser):
    check_page_title = test_browser.find_by_xpath("//div[@class='container']//a[@class='navbar-brand d-flex align-items-center']//span").text
    assert "Shady Meadows B&B" in check_page_title