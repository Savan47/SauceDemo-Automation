from selenium.webdriver.common.by import By
from objects import InventoryPage, CheckoutPage
def test_from_login_to_buy(logged_in_driver, inventory_page, checkout_page):

    inventory_page.add_items_to_cart()
    inventory_page.go_to_cart()
    
    assert "cart.html" in logged_in_driver.current_url
    checkout_page.start_checkout()
    assert "checkout-step-one.html" in logged_in_driver.current_url
    checkout_page.fill_personal_info("Marko", "Polo", "222")
    
    calculated_sum = checkout_page.get_calculated_item_total()
    displayed_sum = checkout_page.get_displayed_subtotal()
    
    assert calculated_sum == displayed_sum, f"Math mismatch! Expected {calculated_sum}, but got {displayed_sum}"
    


  
    assert "checkout-step-two.html" in logged_in_driver.current_url
    checkout_page.finish_order()
    assert checkout_page.get_success_text() == "Thank you for your order!"
    assert "checkout-complete.html" in logged_in_driver.current_url

def test_checkout_error_missing_last_name(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    checkout = CheckoutPage(logged_in_driver)

    inventory.add_items_to_cart()
    inventory.go_to_cart()
    checkout.start_checkout()

    
    checkout.fill_personal_info("Marko", "", "222")

    
    
    assert "Error: Last Name is required" in checkout.get_error_message()