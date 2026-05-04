from selenium import webdriver
import allure
import pytest

@allure.title("Verify that we are able to open the page by using Selenium")
@allure.description("We will open a page and verify that it is getting opened by using Selenium")
def test_first_TC():

    # Selenium 4- No need to use webdriver path

    driver = webdriver.Edge()
    driver.get("https://thetestingacademy.com")
    print(driver.title)
    assert driver.title == "ANC"