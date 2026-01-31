import pytest
from selenium.webdriver.common.by import By



def test_sauce_login_header(logged_in_driver):


    product = logged_in_driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span').text

    assert product == "Products"

def test_login_invalid(driver, login_page):
    driver.get("https://www.saucedemo.com/")
    login_page.type_username("Wrong username")
    login_page.type_password("secret_sauce")
    login_page.click_login()

    result = driver.find_element(By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3').text

    assert result == "Epic sadface: Username and password do not match any user in this service"

@pytest.mark.parametrize("user,password,message", [
    ("pogresan_user", "secret_sauce", "Epic sadface: Username and password do not match any user in this service"),
    ("standard_user", "pogresna_sifra", "Epic sadface: Username and password do not match any user in this service"),
    ("", "secret_sauce", "Epic sadface: Username is required")
])

def test_login_invalid_multiple(driver, login_page, user, password, message):
    driver.get("https://www.saucedemo.com/")
    
    login_page.type_username(user) # uses 'user' from parametrize
    login_page.type_password(password) # uses 'password' from parametrize
    login_page.click_login()
    
    
    
    assert login_page.get_error_message() == message

