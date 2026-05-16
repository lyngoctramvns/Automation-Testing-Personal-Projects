## Automation Testing using Pytest - BDD

Website for testing: (Restful Booker UI Testing Site)[https://automationintesting.online/]

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

