from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver_path = os.path.expanduser(
    r"~\.cache\selenium\chromedriver\win64\155.0.8059.84\chromedriver.exe")


service = Service(executable_path=driver_path)
service.creation_flags = 0x08000000


def test_dynamic_loading():
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
    )
    start_button.click()

    wait = WebDriverWait(driver, 20)

    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#finish"), "Hello World!"))

    hello_element = driver.find_element(By.CSS_SELECTOR, "#finish h4")
    actual_text = hello_element.text

    assert actual_text == "Hello World!"

    driver.save_screenshot("screenshots/full_screen.png")

    driver.quit()
