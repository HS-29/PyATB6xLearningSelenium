import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#@allure.title("app.vwo.com Implicit Waits")
#@allure.description("verify that app.vwo.com is loaded with waits")


def test_project_popup():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver= driver, timeout=10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//span[@data-cy='closeModal']")
        ))

    click_close_popup = driver.find_element(By.XPATH, "//span[@data-cy='closeModal']")
    click_close_popup.click()

    time.sleep(5)
    driver.quit()
