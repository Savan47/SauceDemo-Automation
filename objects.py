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
    