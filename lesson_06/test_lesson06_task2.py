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


def test_session_storage_auth():
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NjM3M2Y0NzMtOTYzNC00YzU0LTgzNjktNTI5YTRkNTI1YjQy",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    driver.get("https://gitflic.ru/user/airsworld")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body")))

    url_1 = driver.current_url
    print(f"URL пользователя 1: {url_1}")

    driver.delete_all_cookies()

    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "ZDBlOGVjMTAtYjVhMi00MzY4LWI1NDgtNTNmNTEyMzIyNjBh",
        "domain": "gitflic.ru"
    })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
    })

    driver.refresh()
    driver.get("https://gitflic.ru/user/cab23c926e")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body")))

    url_2 = driver.current_url
    print(f"URL пользователя 2: {url_2}")

    assert url_1 != url_2, f"Ошибка! URL совпадают: {url_1} == {url_2}"
    print("Тест пройден: URL различаются!")

    driver.quit()
