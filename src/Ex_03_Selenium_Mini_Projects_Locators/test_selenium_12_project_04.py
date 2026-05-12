import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# With positive Test Case
def test_project_idrive360():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(5)

    user_name_input = driver.find_element(By.ID,"username")
    user_name_input.send_keys("augtest_040823@idrive.com")
    time.sleep(2)

    #user_name_input_box = driver.find_element(By.NAME,"username")
    #user_name_input_box.send_keys("John Doe")

    user_password_input = driver.find_element(By.ID,"password")
    user_password_input.send_keys("123456")
    time.sleep(2)

    login_button = driver.find_element(By.ID,"frm-btn")
    login_button.click()
    time.sleep(20)

    #upgrade_now = driver.find_element(By.CLASS_NAME,"id-warning-btn-drk id-tkn-btn")
    #print(upgrade_now.text)
    #assert "Upgrade Now!" == upgrade_now.text
    #time.sleep(5)

    error_message = driver.find_element(By.CLASS_NAME,"id-card-title")
    print(error_message.text)
    assert "Your free trial has expired!" == error_message.text
    time.sleep(5)