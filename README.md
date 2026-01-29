# Selenium UI Automation - SauceDemo Project

This project demonstrates professional UI automation practices using **Python** and **Selenium WebDriver**. It is designed to be scalable, maintainable, and easy to read.

## 🚀 Key Features & Architecture
The framework is built using industry-standard design patterns:
- **Page Object Model (POM)**: Decouples UI locators from test logic for better maintainability.
- **Base Page Inheritance**: Implements a core class for common Selenium actions, reducing code duplication.
- **Pytest Framework**: Utilizes fixtures for efficient browser lifecycle management.
- **Data-Driven Testing (Parametrization)**: Executes multiple login scenarios (valid, invalid, and empty credentials) through a single test function.

📁 Project Structure

objects.py: Contains the BasePage and SouceLoginPage classes.

test_sauce.py: Contains the actual test cases and parametrized data sets.

.gitignore: Prevents temporary files and local reports from cluttering the repository.

🛠️ Installation & Usage

Clone the repository:

Bash
git clone https://github.com/Savan47/SauceDemo-Automation.git
Install dependencies:

Bash
pip install selenium pytest pytest-html webdriver-manager
Run tests and generate report:

Bash
pytest --html=report.html