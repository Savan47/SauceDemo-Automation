# Selenium UI Automation - SauceDemo Project

This project demonstrates professional UI automation practices using **Python** and **Selenium WebDriver**. It is designed to be scalable, maintainable, and easy to read.

## 🚀 Key Features & Architecture
The framework is built using industry-standard design patterns:
- **Page Object Model (POM)**: Decouples UI locators from test logic for better maintainability.
- **Base Page Inheritance**: Implements a core class for common Selenium actions, reducing code duplication.
- **Pytest Framework**: Utilizes fixtures for efficient browser lifecycle management.
- **Data-Driven Testing (Parametrization)**: Executes multiple login scenarios (valid, invalid, and empty credentials) through a single test function.

## 📁 Project Structure
- `objects.py`: Contains the `BasePage` (parent) and `SouceLoginPage` (child) classes.
- `test_sauce.py`: Contains the actual test cases and parametrized data sets.
- `report.html`: Automatically generated HTML report showing test results and execution details.

## 📊 Reporting
The project uses `pytest-html` to generate detailed visual reports. This is essential for tracking test history and identifying bugs quickly.

## 🛠️ Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)