# Pytest fixtures
import pytest
from splinter import Browser

@pytest.fixture(scope="session")
def splinter_webdriver():
    return "chrome"

@pytest.fixture
def test_browser(splinter_webdriver):
    """Fixture to provide a browser instance for testing."""
    browser = Browser(splinter_webdriver)
    browser.visit("https://automationintesting.online/")
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def seed_faker(faker):
    faker.seed_instance(4321)