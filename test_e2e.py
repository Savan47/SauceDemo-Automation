from selenium.webdriver.common.by import By

def test_from_login_to_buy(logged_in_driver):

    driver = logged_in_driver
   
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    

    assert "cart.html" in driver.current_url
    driver.find_element(By.ID, "checkout").click()
    assert "checkout-step-one.html" in driver.current_url
    driver.find_element(By.ID, "first-name").send_keys("Marko")
    driver.find_element(By.ID, "last-name").send_keys("Polo")
    driver.find_element(By.ID, "postal-code").send_keys("222")
    driver.find_element(By.ID, "continue").click()
    assert "checkout-step-two.html" in driver.current_url
    driver.find_element(By.ID, "finish").click()
    assert driver.find_element(By.CLASS_NAME, "complete-header").text == "Thank you for your order!"
    assert "checkout-complete.html" in driver.current_url