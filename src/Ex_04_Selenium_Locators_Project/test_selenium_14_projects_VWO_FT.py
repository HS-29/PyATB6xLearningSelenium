import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# With Negative Test Case
def test_project_app_vwo():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://app.vwo.com/")

    #< input type = "email" class ="text-input W(100%)" name="username" vwo-html-translate-attr="placeholder" vwo-html-translate-placeholder="login:enterEmailID" id="login-username" data-qa="hocewoqisi" placeholder="Enter email ID" >

    user_name_input = driver.find_element(By.XPATH,"//input[@id='login-username']")
    user_name_input.send_keys("HARSHSHARMA@gmail.com")

    #user_name_input_box = driver.find_element(By.NAME,"username")
    #user_name_input_box.send_keys("John Doe")

    user_password_input = driver.find_element(By.XPATH,"//input[@id='login-password']")
    user_password_input.send_keys("This is not a password")

    login_button = driver.find_element(By.ID,"js-login-btn")
    login_button.click()

    # For Certain time
    time.sleep(2)

    error_message = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_message.text)
    assert "Your email, password, IP address or location did not match" == error_message.text

    time.sleep(2)
    anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a FREE TRIAL")
    anchor_tag_element.click()

    #assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(5)


    #driver.quite()



#<a
#href="https://vwo.com/free-trial/?utm_medium=website&amp;utm_source=login-page&amp;utm_campaign=mof_eg_loginpage"
#class="btn Brds(1px) Bdc(--color-gray-5) Bds(s) W(100%)"
#target="_blank" rel="noreferrer"
#style="display:flex; align-items:center; justify-content:center; text-decoration:none;">
#<span>Start a FREE TRIAL</span>
#</a>

# Link Text and Partial Text Concept (This is not related to XPATH but before the XPATH)

# Link Text == Full Exact Match