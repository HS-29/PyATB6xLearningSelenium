import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v145.input_ import MouseButton

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P5")
@allure.description("Verify search options")

def test_verify_actions_makemytrip():
    chrome_options = Options()
    #chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    #chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.spicejet.com/")

    from_city = driver.find_element(By.XPATH,"//input[@autocapitalize='sentences']")

    actions = ActionChains(driver=driver)
    actions.move_to_element(from_city).click().send_keys_to_element(from_city,"del").perform()
    time.sleep(2)
    #actions.move_to_element(from_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    to_city = driver.find_element(By.XPATH,"//input[@autocapitalize='sentences']")

    actions = ActionChains(driver=driver)
    actions.move_to_element(to_city).click().send_keys_to_element(to_city,"ixc").perform()
    #time.sleep(2)
    #actions.move_to_element(to_city).key_down(Keys.ARROW_DOWN).key_up(Keys.ENTER).perform()

    time.sleep(10)
    driver.quit()