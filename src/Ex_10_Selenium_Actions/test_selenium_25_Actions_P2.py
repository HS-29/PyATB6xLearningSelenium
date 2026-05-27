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

@allure.title("Actions P2")
@allure.description("Verify Mouse back")

def test_verify_actions_mouse():
    chrome_options = Options()
    chrome_options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    results_page = driver.find_element(By.ID,'click')
    results_page.click()

    time.sleep(2)
    driver.back()

    #actions = ActionChains(driver=driver)
    #actions.move_to_element(results_page).context_click().perform()

    #actions_builder = ActionBuilder(driver=driver)
    #actions_builder.pointer_action.pointer_up(MouseButton.RIGHT).perform()

    time.sleep(10)
    driver.quit()