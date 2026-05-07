import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import *

# With Positive Test Case
def test_project1_katalon():
    chrome_options = Options()
    chrome_options.add_argument("--start maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    #time.sleep(5)

    user_name_input = driver.find_element(By.ID,"txt-username")
    user_name_input.send_keys("John Doe")
    #user_name_input_box = driver.find_element(By.NAME,"username")
    #user_name_input_box.send_keys("John Doe")

    user_password_input = driver.find_element(By.ID,"txt-password")
    user_password_input.send_keys("ThisIsNotAPassword")

    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()

    time.sleep(2)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)



import time
#from calendar import error
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import *

# With Negative Test Case
def test1_project1_katalon():
    chrome_options = Options()
    chrome_options.add_argument("--start maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment_element.click()
    #time.sleep(5)

    user_name_input = driver.find_element(By.ID,"txt-username")
    user_name_input.send_keys("Doe John")
    #user_name_input_box = driver.find_element(By.NAME,"username")
    #user_name_input_box.send_keys("John Doe")

    user_password_input = driver.find_element(By.ID,"txt-password")
    user_password_input.send_keys("WrongAPassword")

    login_button = driver.find_element(By.ID,"btn-login")
    login_button.click()

    time.sleep(2)
    error_message = driver.find_element(By.CLASS_NAME,"text-danger")
    print(error_message.text)
    assert "Login failed! Please ensure the username and password are valid."==error_message.text

    #assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    time.sleep(5)


# <p
# class="lead text-danger">Login failed! Please ensure the username and password are valid.
# </p>