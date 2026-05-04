from selenium import webdriver
import allure
import pytest

@allure.title("Verify that we are able to open the page by using Selenium")
@allure.description("We will open a page and verify that it is getting opened by using Selenium")
def test_first_TC():

    # Selenium 3(Use Webdriver path)- not used much now
    #driver_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    #driver = webdriver.Edge(driver_path)

    driver = webdriver.Chrome()
    driver.get("https://thetestingacademy.com")
    print(driver.title)
    assert driver.title == "ANC"