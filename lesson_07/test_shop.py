from selenium import webdriver
from shop_pages import LoginPage, MainPage, CartPage, CheckoutPage


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    try:
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        main_page.add_to_cart(MainPage.BACKPACK)
        main_page.add_to_cart(MainPage.BOLT_TSHIRT)
        main_page.add_to_cart(MainPage.ONESIE)

        main_page.click_cart()

        cart_page.click_checkout()

        checkout_page.fill_form("Мария", "Марьевна", "123456")
        checkout_page.click_continue()

        total_text = checkout_page.get_total()
        assert "$58.29" in total_text, (
            f"Ожидалась сумма $58.29, получено: {total_text}"
        )
    finally:
        driver.quit()
