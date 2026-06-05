## Automation Testing using Pytest - BDD

Website for E2E testing: [Restful Booker UI Testing Site](https://automationintesting.online/)

API testing script for Restful Booker: [API documentation](https://restful-booker.herokuapp.com/apidoc/index.html)

To run the test suites with local booking site, clone the following repo and follow the instructions:

[Restful-booker-platform](https://github.com/mwinteringham/restful-booker-platform)

Using Gherkin - BDD to test on Pytest

### How to run:

#### Pre-requisites:

install venv and dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
.env - See the above for the site url link. Or if you run locally, set the localhost url in the .env file.

```bash
SITE_URL=""
```

1. Run a specific E2E test suite
```bash
python -m pytest e2e/steps/$file_name.py
```
2. Run the entire E2E test suites folder
```bash
python -m pytest e2e/steps/
```

### How to generate reports:
1. Generate allure-results
```bash
python -m pytest --alluredir allure-results
```
2. 
    1. If you have Nodejs installed, run:
    ```bash
    npx allure-commandline serve allure-results
    ```
   2. If not, using pytest-report:
    ```bash
    pip install pytest-html
    python -m pytest --html=report.html --self-contained-html
    start report.html
    ```
**NOTE:** For actual tests, developers are asked to include test classes/ test ids to catch as locators.

### Github Actions:

Will be run in a separate repo. The result is shown below:
