from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_input = self.wait.until(
            EC.presence_of_element_located(self.USERNAME_INPUT)
        )
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.wait.until(
            EC.presence_of_element_located(self.PASSWORD_INPUT)
        )
        password_input.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_button.click()


class MainPage:
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def add_to_cart(self, locator):
        item = self.wait.until(
            EC.element_to_be_clickable(locator)
        )
        item.click()

    def click_cart(self):
        cart_button = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )
        cart_button.click()


class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_checkout(self):
        checkout_button = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        checkout_button.click()


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_SUM = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def fill_form(self, first_name, last_name, postal_code):
        first_name_input = self.wait.until(
            EC.presence_of_element_located(self.FIRST_NAME_INPUT)
        )
        first_name_input.send_keys(first_name)

        last_name_input = self.wait.until(
            EC.presence_of_element_located(self.LAST_NAME_INPUT)
        )
        last_name_input.send_keys(last_name)

        postal_code_input = self.wait.until(
            EC.presence_of_element_located(self.POSTAL_CODE)
        )
        postal_code_input.send_keys(postal_code)

    def click_continue(self):
        continue_button = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )
        continue_button.click()

    def get_total(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_SUM)
        )
        return total_element.text
