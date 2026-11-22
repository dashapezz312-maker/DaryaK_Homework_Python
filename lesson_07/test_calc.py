from selenium import webdriver
from calc_pages import CalcPage


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    try:
        page = CalcPage(
            driver,
            "https://bonigarcia.dev/selenium-webdriver-"
            "java/slow-calculator.html"
        )
        page.open_calc_page()
        page.set_delay(45)
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")
        page.wait_for_result("15")
        assert page.get_sum_result() == "15"

    finally:
        driver.quit()
