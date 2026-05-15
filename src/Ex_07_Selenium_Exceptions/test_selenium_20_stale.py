import time
import allure
import pytest

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException


@allure.title("stale exception")
@allure.description("verify stale exception")

def test_stale_exception():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME, 'q')
        driver.refresh()
        textarea.send_keys("The Testing Academy")
        #print(textarea.text)
        print("End of test case")
    except StaleElementReferenceException as see:
        print(see.msg)
    time.sleep(5)
    driver.quit()