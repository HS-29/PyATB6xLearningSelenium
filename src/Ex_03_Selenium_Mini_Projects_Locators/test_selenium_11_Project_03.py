import time
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

    user_name_input = driver.find_element(By.ID,"login-username")
    user_name_input.send_keys("HARSHSHARMA@gmail.com")

    #user_name_input_box = driver.find_element(By.NAME,"username")
    #user_name_input_box.send_keys("John Doe")

    user_password_input = driver.find_element(By.ID,"login-password")
    user_password_input.send_keys("This is not a password")

    login_button = driver.find_element(By.ID,"js-login-btn")
    login_button.click()

    time.sleep(2)

    error_message = driver.find_element(By.ID,"js-notification-box-msg")
    print(error_message.text)
    assert "Your email, password, IP address or location did not match"==error_message.text

    time.sleep(5)
