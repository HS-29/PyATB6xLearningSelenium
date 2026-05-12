import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.title("app.vwo.com Implicit Waits")
@allure.description("verift that app.vwo.com is loaded with waits")


def test_project_alert_js_simple():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #click_js_alert = driver.find_element(By.XPATH, "//button[contains (text(), 'Click for JS Alert')]")
    click_js_alert = driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    click_js_alert.click()

    # Explicit wait that we have added.
    WebDriverWait(driver=driver,timeout= 5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()

    result_text = driver.find_element(By.ID, "result").text
    #print(result_text.text)
    #assert result_text.text == "You successfully clicked an alert"
    assert result_text == "You successfully clicked an alert"

    time.sleep(5)
    driver.quit()


def test_project_alert_js_confirm():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #click_js_alert = driver.find_element(By.XPATH, "//button[contains (text(), 'Click for JS Alert')]")
    click_js_alert_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")
    click_js_alert_confirm.click()

    # Explicit wait that we have added.
    WebDriverWait(driver=driver,timeout= 5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    #alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text
    #print(result_text.text)
    #assert result_text.text == "You successfully clicked an alert"
    assert result_text == "You clicked: Cancel"

    time.sleep(5)
    driver.quit()


def test_project_alert_js_prompt():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    #click_js_alert = driver.find_element(By.XPATH, "//button[contains (text(), 'Click for JS Alert')]")
    click_js_alert_prompt = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    click_js_alert_prompt.click()

    # Explicit wait that we have added.
    WebDriverWait(driver=driver,timeout= 5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.send_keys("I am experienced QA")
    alert.accept()
    #alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text
    #print(result_text.text)
    #assert result_text.text == "You successfully clicked an alert"
    assert result_text == "You entered: I am experienced QA"

    time.sleep(5)
    driver.quit()


