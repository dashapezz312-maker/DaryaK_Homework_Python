from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:
    SECONDS_INPUT = (By.ID, "delay")
    RESULT_FIELD = (By.CLASS_NAME, "screen")
    RESULT_TIMEOUT = 46

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 10)

    def open_calc_page(self):
        self.driver.get(self.url)

    def set_delay(self, seconds):
        seconds_input = self.wait.until(
            EC.presence_of_element_located(self.SECONDS_INPUT)
        )
        seconds_input.clear()
        seconds_input.send_keys(str(seconds))

    def click_button(self, label):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{label}']"
        ).click()

    def wait_for_result(self, expected_text, timeout=RESULT_TIMEOUT):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.RESULT_FIELD, expected_text)
        )

    def get_sum_result(self):
        return self.driver.find_element(*self.RESULT_FIELD).text
