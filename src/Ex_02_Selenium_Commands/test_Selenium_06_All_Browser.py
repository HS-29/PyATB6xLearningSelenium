from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
import pytest
import time


def test_chrome_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()

def test_edge_url_verification():
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    time.sleep(10)
    driver.quit()


#def test_currrent_url_verification():
#   driver = webdriver.firefox()
#   driver.get("https://katalon-demo-cura.herokuapp.com/")
#   time.sleep(10)
#   driver.quit()