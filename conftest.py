import pytest
import os
from selenium import webdriver
from objects import SouceLoginPage, InventoryPage, CheckoutPage, CartPage
from selenium.webdriver.chrome.options import Options
import logging
import allure


# Logging configuration: Allows us to track test execution steps in the console
def pytest_configure(config):
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
# --- PAGE OBJECT FIXTURES ---
# These fixtures provide easy access to Page Objects, keeping tests clean and readable
@pytest.fixture
def cart_page(logged_in_driver):
    return CartPage(logged_in_driver)


@pytest.fixture
def inventory_page(logged_in_driver):
    return InventoryPage(logged_in_driver)

@pytest.fixture
def checkout_page(logged_in_driver):
    return CheckoutPage(logged_in_driver)

@pytest.fixture
def login_page(driver):
    from objects import SouceLoginPage
    return SouceLoginPage(driver)
# Main WebDriver fixture: Handles browser setup and teardown
@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--maximize-window")

   

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    
    # --- TEARDOWN LOGIC (Post-test execution) ---
    
    # Check if the test case has failed
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        # Create a screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        file_name = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(file_name)
    # Attach the screenshot to the Allure Report for better debugging
    allure.attach(
            driver.get_screenshot_as_png(),
            name=f"Screenshot_{request.node.name}",
            attachment_type=allure.attachment_type.PNG
    )
    driver.quit() # Close the browser session
    
# Fixture to automate the login process as a precondition for main features
@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = SouceLoginPage(driver)
    login_page.type_username("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login()
    return driver
    
# Pytest Hook: Used to capture the test result (Passed/Failed)
# This allows the 'driver' fixture to know when to trigger a screenshot
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
