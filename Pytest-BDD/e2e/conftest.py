# Pytest fixtures
import os
from dotenv import load_dotenv, dotenv_values
import pytest
from splinter import Browser

load_dotenv()

@pytest.fixture(scope="session")
def splinter_webdriver():
    return "chrome"

@pytest.fixture
def test_browser(splinter_webdriver):
    """Fixture to provide a browser instance for testing."""
    browser = Browser(splinter_webdriver)
    browser.visit(os.getenv("SITE_URL"))
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def seed_faker(faker):
    faker.seed_instance(4321)