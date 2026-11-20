from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.find_element(By.NAME, "custname").send_keys("Дарья")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    sleep(3)

    assert driver.current_url == "https://httpbin.qa-territory.online/post"

    driver.quit()
