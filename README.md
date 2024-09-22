# Assignment

This project automates the search and cart functionality on Amazon using Python, Pytest, and Selenium, following the Page Object Model (POM) design pattern.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation Steps](#installation-steps)
- [Project Structure](#project-structure)
- [Page Object Model (POM)](#page-object-model-pom)
- [Running Tests](#running-tests)
- [Generating Reports](#generating-reports)
- [Contributing](#contributing)

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.x installed on your machine
- pip (Python package installer) is installed

## Installation Steps

Follow these steps to set up the project:

1. **Create Project Root Folder**
   ```bash
   mkdir Amazon
   cd Amazon
   
2. **Install Requirements from requirements.txt**
   Ensure you have a requirements.txt file in the root directory containing necessary packages (e.g., Selenium, Pytest).
   pip install -r requirements.txt

3. **Create Folder for Tests**
   mkdir tests
   This folder will contain all the Pytest scripts.
   
4. **Create Folder for Pages**
   mkdir pages
   This folder will contain Python files implementing the Page Object Model.

5. **Project Structure**
   Your project directory should look like this:
   
   Amazon/
│
├── venv/                  # Virtual environment
├── requirements.txt       # Dependencies
├── tests/                 # Folder containing Pytest scripts
│   ├── test_amazon.py     # Test file using POM
│   └── test_amazon-original.py  # Original test file without POM
└── pages/                 # Folder containing Page Object Model classes
    ├── amazon_page.py     # Page object for the Amazon homepage and search functionality
    ├── cart_page.py       # Page object for cart operations
    └── search_results_page.py  # Page object for handling search results


6. **Page Object Model (POM)**
The Page Object Model is a design pattern that enhances test maintenance and reduces code duplication. Each page of the application is represented by a separate class, encapsulating its elements and actions. This structure allows for better organization and easier updates to the tests.

7.**Running Tests**
   pytest tests/
**Test Files**
test_amazon.py: This test file uses the Page Object Model (POM) to structure the tests for improved maintainability.
test_amazon-original.py: This is the original test file that contains pure scripts without using POM.


8. **Generating Reports**
   To generate test reports, you can use plugins such as pytest-html. Install it via pip:


pip install pytest-html
Run the tests with the report option:


pytest --html=report.html
This will create a report.html file in the project root that summarizes the test results.




