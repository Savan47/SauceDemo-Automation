from selenium.webdriver.common.by import By


def test_products_page(logged_in_driver):


    titleproducts = logged_in_driver.find_element(By.CLASS_NAME, "title").text

    assert titleproducts == "Products"

    items = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    assert len(items) == 6

    button = logged_in_driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    assert button.text == "Add to cart" # SauceDemo koristi velika slova!
    button.click()

    remove_button = logged_in_driver.find_element(By.CSS_SELECTOR, "#remove-sauce-labs-backpack")
    assert remove_button.text == "Remove"

    badge = logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"