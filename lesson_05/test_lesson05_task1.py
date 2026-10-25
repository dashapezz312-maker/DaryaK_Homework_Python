from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lesson05_task1():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    assert driver.current_url == "https://httpbin.qa-territory.online/"
    "forms/post"

    driver.back()

    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit
