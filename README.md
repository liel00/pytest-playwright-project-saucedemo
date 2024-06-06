
# Pytest Playwright Project Saucedemo

This repository contains a test automation project using Pytest and Playwright for the SauceDemo web application.

## Table of Contents
- [Introduction](#introduction)
- [Setup](#setup)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Writing Tests](#writing-tests)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project uses Pytest, a popular testing framework for Python, and Playwright, a tool for browser automation, to test the SauceDemo web application. The goal is to ensure the functionality and reliability of the web application through automated tests.

## Setup
To get started with this project, follow these steps:

1. **Clone the repository:**
    \`\`\`bash
    git clone https://github.com/liel00/pytest-playwright-project-saucedemo.git
    cd pytest-playwright-project-saucedemo
    \`\`\`

2. **Create a virtual environment and activate it:**
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
    \`\`\`

3. **Install the required dependencies:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4. **Install Playwright browsers:**
    \`\`\`bash
    playwright install
    \`\`\`

## Running Tests
To run the tests, use the following command:
\`\`\`bash
pytest
\`\`\`
This will execute all the tests in the project and generate a test report.

## Project Structure
The project is organized as follows:
\`\`\`
.
├── tests
│   ├── test_login.py
│   ├── test_cart.py
│   └── ...
├── pages
│   ├── login_page.py
│   ├── cart_page.py
│   └── ...
├── conftest.py
├── requirements.txt
├── pytest.ini
└── README.md
\`\`\`

- `tests/` - Contains the test files.
- `pages/` - Contains the page object model (POM) files, which abstract the interactions with different pages of the web application.
- `conftest.py` - Configuration file for Pytest, including fixtures.
- `requirements.txt` - List of dependencies.
- `pytest.ini` - Pytest configuration file.

## Writing Tests
To add a new test, create a new file in the `tests/` directory and define your test functions using Pytest conventions. You can use the page objects from the `pages/` directory to interact with the web application.

Example:
\`\`\`python
from pages.login_page import LoginPage

def test_login_valid_user(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login('standard_user', 'secret_sauce')
    assert login_page.is_logged_in()
\`\`\`

## Contributing
Contributions are welcome! Please create an issue or submit a pull request for any improvements, bug fixes, or new features.

1. Fork the repository.
2. Create a new branch: \`git checkout -b my-feature-branch\`
3. Make your changes and commit them: \`git commit -m 'Add some feature'\`
4. Push to the branch: \`git push origin my-feature-branch\`
5. Submit a pull request.


"""



