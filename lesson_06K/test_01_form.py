from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    wait = WebDriverWait(driver, 10)

    first_name_input = wait.until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )
    first_name_input.send_keys("Иван")

    last_name_input = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "last-name")))
    last_name_input.send_keys("Петров")

    address_input = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "address")))
    address_input.send_keys("Ленина, 55-3")

    email_input = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "e-mail")))
    email_input.send_keys("test@skypro.com")

    phone_number_input = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "phone")))
    phone_number_input.send_keys("+7985899998787")

    city_input = wait.until(EC.presence_of_element_located((By.NAME, "city")))
    city_input.send_keys("Москва")

    country_input = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "country")))
    country_input.send_keys("Россия")

    job_position_input = wait.until(
        EC.presence_of_element_located((By.NAME, "job-position"))
    )
    job_position_input.send_keys("QA")

    company_input = wait.until(
        EC.presence_of_element_located(
            (By.NAME, "company")))
    company_input.send_keys("SkyPro")

    submit_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    wait.until(EC.url_contains("data-types-submitted.html"))

    zip_code_input = wait.until(
        EC.presence_of_element_located(
            (By.ID, "zip-code")))
    zip_color = zip_code_input.value_of_css_property("border-bottom-color")

    assert zip_color == "rgba(245, 194, 199, 1)", (
        f"Zip code не красный: {zip_color}"
    )

    green_field_ids = [
        "first-name",
        "last-name",
        "address",
        "e-mail",
        "phone",
        "city",
        "country",
        "job-position",
        "company",
    ]

    for field_id in green_field_ids:
        field = driver.find_element(By.ID, field_id)
        field_color = field.value_of_css_property("border-bottom-color")

        assert (
            field_color == "rgba(186, 219, 204, 1)"
        ), f"Поле {field_id} не зеленое: {field_color}"

    driver.quit()
