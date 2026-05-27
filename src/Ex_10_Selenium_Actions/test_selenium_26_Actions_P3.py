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

def test_verify_actions_mouse():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag_element = driver.find_element(By.ID,'draggable')
    time.sleep(5)

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element = drag_element).perform()

    time.sleep(10)
    driver.quit()