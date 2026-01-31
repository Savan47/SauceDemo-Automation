import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from objects import SouceLoginPage
import os




@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver

    report = getattr(request.node, "rep_call", None)

    if report and report.failed:
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")
        file_name = f"screenshots/{request.node.name}.png"
        driver.save_screenshot(file_name)
        print(f"\n Screenshot saved: {file_name}")

    driver.quit()




def test_sauce_login(driver):
    driver.get("https://www.saucedemo.com/")
    ulaz = SouceLoginPage(driver)
    ulaz.type_username("standard_user")
    ulaz.type_password("secret_sauce")
    ulaz.click_login()

    product = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text

    assert product == "Products"

def test_login_invalid(driver):
    driver.get("https://www.saucedemo.com/")
    ulaz = SouceLoginPage(driver)
    ulaz.type_username("standard_user123")
    ulaz.type_password("secret_sauce")
    ulaz.click_login()

    result = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text

    assert result == "Epic sadface: Username and password do not match any user in this service"

@pytest.mark.parametrize("user,password,message", [
    ("pogresan_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "pogresna_sifra", "Epic sadface: Username and password do not match any user in this service"),
    ("", "secret_sauce", "Epic sadface: Username is required")
])

def test_login_invalid_multiple(driver, user, password, message):
    driver.get("https://www.saucedemo.com/")
    ulaz = SouceLoginPage(driver)
    
    ulaz.type_username(user) # uses 'user' from parametrize
    ulaz.type_password(password) # uses 'password' from parametrize
    ulaz.click_login()
    
    
    
    assert ulaz.get_error_message() == message



