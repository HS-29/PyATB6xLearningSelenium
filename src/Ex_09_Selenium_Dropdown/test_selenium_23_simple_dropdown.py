import time
import allure
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("SVG")
@allure.description("verify SVG")

def test_svg():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://the-internet.herokuapp.com/dropdown")

    select_html_tag= driver.find_element(By.ID, 'dropdown')
    #select_html_tag.click()
    select = Select(select_html_tag)
    #select.select_by_value("1")
    #select.select_by_value("2")
    select.select_by_value("1")

    element_selenium = driver.find_element(By.XPATH,"//a[@target='_blank']")
    element_selenium.click()

    time.sleep(5)
