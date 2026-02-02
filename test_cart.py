import logging
from selenium.webdriver.common.by import By


def test_remove_cart(inventory_page, cart_page):
    logging.info("--- Starting Remove items in Cart Test ---")

    inventory_page.add_items_to_cart()
    logging.info("Items added to cart successfully")
    inventory_page.go_to_cart()
    cart_page.click_remove_btn()
    assert cart_page.get_cart_badge_text() == "1"

def test_0_products(inventory_page, cart_page):
    logging.info("--- Starting 0 items in Cart Test ---")

    inventory_page.add_items_to_cart()
    inventory_page.go_to_cart()
    logging.info("Items added to cart successfully")

    cart_page.click_remove_btn()
    cart_page.click_remove_btn()
    inventory_page.go_to_cart()
    assert cart_page.is_badge_displayed() == False