import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.common.exceptions import NoSuchElementException


@allure.title("exception handel")
@allure.description("verify exception_handling")

def test_exception_handling():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com")
    try:
        element = driver.find_element(By.ID, "this_id_username_does_not_exist")
    except NoSuchElementException as nse:
        #print("NoSuchElementException")
        print(nse.msg)