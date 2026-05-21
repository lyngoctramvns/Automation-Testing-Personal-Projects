## Automation Testing using Pytest - BDD

Website for testing: [Restful Booker UI Testing Site](https://automationintesting.online/)

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


1. Run a specific test suite
```bash
python -m pytest steps/$file_name.py
```
2. Run the entire test suites folder
```bash
python -m pytest steps/
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

