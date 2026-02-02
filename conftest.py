import pytest
import os
from selenium import webdriver
from objects import SouceLoginPage, InventoryPage, CheckoutPage
from selenium.webdriver.chrome.options import Options


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

@pytest.fixture
def driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--maximize-window")

   

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    
    
    report = getattr(request.node, "rep_call", None)
    if report and report.failed:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        file_name = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(file_name)
    
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = SouceLoginPage(driver)
    login_page.type_username("standard_user")
    login_page.type_password("secret_sauce")
    login_page.click_login()
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)