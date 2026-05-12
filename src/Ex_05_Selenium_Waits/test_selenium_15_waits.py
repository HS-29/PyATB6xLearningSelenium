import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("app.vwo.com Implicit Waits")
@allure.description("verift that app.vwo.com is loaded with waits")

def test_project_app_vwo():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")

    #driver.implicitly_wait(5)--> We are going to use only 0.01% in automation scripts.


    user_name_input = driver.find_element(By.XPATH, "//input[@id='login-username']")
    user_name_input.send_keys("HARSHSHARMA@gmail.com")

    user_password_input = driver.find_element(By.XPATH, "//input[@id='login-password']")
    user_password_input.send_keys("Wrong password")

    login_button =driver.find_element(By.ID, "js-login-btn")
    login_button.click()

    #Explicit wait we are using in automation scripts
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "notification-box-description")))

    error_message = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_message.text)
    assert "Your email, password, IP address or location did not match" == error_message.text