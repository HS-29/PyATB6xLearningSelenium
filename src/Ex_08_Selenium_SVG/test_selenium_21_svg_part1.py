import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("verify SVG")

def test_svg():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.flipkart.com/")

    #search box
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("macmini")

    time.sleep(2)

    list_svg_element = driver.find_elements(By.XPATH, "//*[name()='svg']")
    #list_svg_element = driver.find_elements(By.XPATH, "//button[@type='submit']//*[name()='svg']")
    list_svg_element[0].click()

    time.sleep(5)
    driver.quit()
