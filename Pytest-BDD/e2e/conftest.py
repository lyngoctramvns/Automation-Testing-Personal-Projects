# Pytest fixtures
import os
from dotenv import load_dotenv, dotenv_values
import pytest
from selenium.webdriver import ChromeOptions
from splinter import Browser

load_dotenv()

@pytest.fixture(scope="session")
def splinter_webdriver():
    return "chrome"

@pytest.fixture
def test_browser(splinter_webdriver):
    """Fixture to provide a browser instance for testing."""
    chrome_options = ChromeOptions()
    
    # Add arguments for CI/CD GitHub Actions environment
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")  # Bypass OS security
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--window-size=1920,1080")  # Set window size for consistent rendering

    browser = Browser(splinter_webdriver, options=chrome_options)
    browser.visit(os.getenv("SITE_URL"))
    yield browser
    browser.quit()

@pytest.fixture(autouse=True)
def seed_faker(faker):
    faker.seed_instance(4321)