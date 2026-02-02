from selenium.webdriver.common.by import By
from objects import InventoryPage, CheckoutPage
def test_from_login_to_buy(logged_in_driver):

    #driver = logged_in_driver
    inventory = InventoryPage(logged_in_driver)
    checkout = CheckoutPage(logged_in_driver)
    inventory.add_items_to_cart()
    inventory.go_to_cart()
    
    assert "cart.html" in logged_in_driver.current_url
    checkout.start_checkout()
    assert "checkout-step-one.html" in logged_in_driver.current_url
    checkout.fill_personal_info("Marko", "Polo", "222")
  
    assert "checkout-step-two.html" in logged_in_driver.current_url
    checkout.finish_order()
    assert checkout.get_success_text() == "Thank you for your order!"
    assert "checkout-complete.html" in logged_in_driver.current_url

def test_checkout_error_missing_last_name(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    checkout = CheckoutPage(logged_in_driver)

    inventory.add_items_to_cart()
    inventory.go_to_cart()
    checkout.start_checkout()

    
    checkout.fill_personal_info("Marko", "", "222")

    
    error_text = logged_in_driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Error: Last Name is required" in error_text