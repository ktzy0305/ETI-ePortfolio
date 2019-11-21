import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_login_no_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/login?next=/")
    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    login_btn_elem.click()
    return

def test_login_wrong_password():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/login?next=/")

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("David3k")
    password_elem.send_keys("red50blue")

    login_btn_elem.click()

    time.sleep(3)

    error_elem = driver.find_element_by_xpath('//*[@id="login-form"]/form/p')
    assert error_elem.text == "Incorrect Username or Password!"

def test_login_unregistered_user():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/login?next=/")

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')
    
    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("Dred6")
    password_elem.send_keys("password")

    login_btn_elem.click()

    time.sleep(3)

    error_elem = driver.find_element_by_xpath('//*[@id="login-form"]/form/p')
    assert error_elem.text == "Incorrect Username or Password!"


def test_login_correct_credentials():
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

    welcome_username_span_elem = driver.find_element_by_xpath('//*[@id="home-alert-container"]/div/span')
    assert welcome_username_span_elem.text == "David3k"

def test_login_form_click_back():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/")

    login_nav_item_elem = driver.find_element_by_xpath('//*[@id="nav-menu"]/li[3]/a')
    login_nav_item_elem.click()

    time.sleep(5)

    login_form_back_btn = driver.find_element_by_xpath('//*[@id="login-form"]/a')
    login_form_back_btn.click()

    time.sleep(5)

    assert driver.title == "Kevin's Blog"

def test_login_form_click_register():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/login?next=/")

    register_account_elem = driver.find_element_by_xpath('//*[@id="login-form-options"]/li/a')
    register_account_elem.click()

    time.sleep(5)

    assert driver.title == "Kevin's Blog | Account Registration"

    return