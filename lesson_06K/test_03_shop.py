from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    wait = WebDriverWait(driver, 10)

    username_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "user-name")))
    username_input.send_keys("standard_user")

    password_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "password")))
    password_input.send_keys("secret_sauce")

    login_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "login-button")))
    login_button.click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    first_name_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "first-name")))
    first_name_input.send_keys("Мария")

    last_name_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "last-name")))
    last_name_input.send_keys("Марьевна")

    postal_code_input = wait.until(
        EC.presence_of_element_located((By.ID, "postal-code"))
    )
    postal_code_input.send_keys("123456")

    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    total_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )

    total_text = total_element.text

    assert "$58.29" in total_text, (
        f"Ожидалась сумма $58.29, получено: {total_text}"
    )

    driver.quit()
