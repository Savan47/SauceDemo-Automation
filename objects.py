from selenium.webdriver.common.by import By


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

class SouceLoginPage(BasePage):
        #Locators
    user_name = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def type_username(self, user):
        self.find_element(self.user_name).send_keys(user)

    def type_password(self, pass1):
        self.find_element(self.password).send_keys(pass1)

    def click_login(self):
        self.find_element(self.login_button).click()
    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
    

class InventoryPage(BasePage):
    # Locators
    backpack_add_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    bike_light_add_btn = (By.ID, "add-to-cart-sauce-labs-bike-light")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")

    def add_items_to_cart(self):
        self.find_element(self.backpack_add_btn).click()
        self.find_element(self.bike_light_add_btn).click()

    def go_to_cart(self):
        self.find_element(self.cart_icon).click()

class CheckoutPage(BasePage):
    # Locators
    checkout_btn = (By.ID, "checkout")
    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_btn = (By.ID, "continue")
    finish_btn = (By.ID, "finish")
    success_msg = (By.CLASS_NAME, "complete-header")

    def start_checkout(self):
        self.find_element(self.checkout_btn).click()

    def fill_personal_info(self, name, surname, zip_code):
        self.find_element(self.first_name).send_keys(name)
        self.find_element(self.last_name).send_keys(surname)
        self.find_element(self.postal_code).send_keys(zip_code)
        self.find_element(self.continue_btn).click()

    def finish_order(self):
        self.find_element(self.finish_btn).click()

    def get_success_text(self):
        return self.find_element(self.success_msg).text