import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_log_out():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    login_nav_item_elem = driver.find_element_by_xpath('//*[@id="nav-menu"]/li[3]/a')
    login_nav_item_elem.click()

    time.sleep(5)

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("David3k")
    password_elem.send_keys("Cyan30red")

    login_btn_elem.click()
    
    time.sleep(5)

    logout_nav_item_elem = driver.find_element_by_xpath('//*[@id="nav-menu"]/li[3]/a')
    logout_nav_item_elem.click()

    test_login_nav_item_elem = driver.find_element_by_xpath('//*[@id="nav-menu"]/li[3]/a')

    assert test_login_nav_item_elem.text == "LOGIN"