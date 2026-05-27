import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_verify_actions_keyboard():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.NAME, 'firstname')
    #first_name = driver.find_element(By.XPATH, "//input[@name='firstname']")
    first_name.click()
    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"harsh").key_up(Keys.SHIFT).perform()

    last_name= driver.find_element(By.NAME, 'lastname')
    last_name.click()
    #actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(last_name,"sharma").key_up(Keys.SHIFT).perform()

    gender_male = driver.find_element(By.ID, 'sex-0')
    gender_male.click()

    year_experience = driver.find_element(By.ID,'exp-5')
    year_experience.click()

    
    time.sleep(10)
    driver.quit()