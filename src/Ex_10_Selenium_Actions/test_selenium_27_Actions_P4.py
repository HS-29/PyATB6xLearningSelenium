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

@allure.title("Actions P3")
@allure.description("Verify Drag element")

def test_verify_actions_makemytrip():
    chrome_options = Options()
    #chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--start-maximized')
    #chrome_options.add_argument('--incognito')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//span[@data-cy='closeModal']")))
    driver.find_element(By.XPATH,"//span[@data-cy='closeModal']").click()

    from_city = driver.find_element(By.ID,'fromCity')

    actions = ActionChains(driver=driver)
    actions.move_to_element(from_city).click().send_keys_to_element(from_city,"del").perform()
    time.sleep(2)
    actions.move_to_element(from_city).key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

    to_city = driver.find_element(By.ID,'toCity')

    actions = ActionChains(driver=driver)
    actions.move_to_element(to_city).click().send_keys_to_element(to_city,"ixc").perform()
    time.sleep(2)
    actions.move_to_element(to_city).key_down(Keys.ARROW_DOWN).key_up(Keys.ENTER).perform()

    time.sleep(10)
    driver.quit()