from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import os

driver_path = os.path.expanduser(
    r"~\.cache\selenium\chromedriver\win64\155.0.8059.84\chromedriver.exe"
)


service = Service(executable_path=driver_path)
service.creation_flags = 0x08000000


def test_calc():
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 10)

    Seconds_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "delay")))
    Seconds_input.clear()
    Seconds_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    long_wait = WebDriverWait(driver, 46)

    long_wait.until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"))

    result = driver.find_element(By.CLASS_NAME, "screen")
    assert result.text == "15"

    driver.quit()
