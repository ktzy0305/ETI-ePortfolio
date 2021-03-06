import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User
import time

def test_registration_no_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    driver.execute_script("arguments[0].removeAttribute('required')", email_input_elem)
    driver.execute_script("arguments[0].removeAttribute('required')", username_input_elem)
    driver.execute_script("arguments[0].removeAttribute('required')", password_input_elem)
    driver.execute_script("arguments[0].removeAttribute('required')", confirm_password_input_elem)

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    register_btn_elem.click()
    assert driver.title == "Kevin's Blog | Account Registration"


def test_registration_invalid_email():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    # Change type attribute of email element to text
    driver.execute_script("arguments[0].setAttribute('type', 'text')", email_input_elem)

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    email_input_elem.send_keys("jack#mail.com")
    username_input_elem.send_keys("Jack20")
    password_input_elem.send_keys("P@ssw0rd")
    confirm_password_input_elem.send_keys("P@ssw0rd")

    register_btn_elem.click()

    email_error_elem = driver.find_element_by_xpath('//*[@id="register-form-box"]/div[1]/span')
    assert email_error_elem.text == "Email has invalid format."


def test_registration_existing_email():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    email_input_elem.send_keys("d3k@mail.com")
    username_input_elem.send_keys("Jack20")
    password_input_elem.send_keys("P@ssw0rd")
    confirm_password_input_elem.send_keys("P@ssw0rd")

    register_btn_elem.click()

    time.sleep(2)

    email_error_elem = driver.find_element_by_xpath('//*[@id="register-form-box"]/div[1]/span')
    assert email_error_elem.text == "An account with this email already exists."


def test_registration_existing_username():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    email_input_elem.send_keys("jack@mail.com")
    username_input_elem.send_keys("David3k")
    password_input_elem.send_keys("P@ssw0rd")
    confirm_password_input_elem.send_keys("P@ssw0rd")

    register_btn_elem.click()

    time.sleep(2)

    username_error_elem = driver.find_element_by_xpath('//*[@id="register-form-box"]/div[2]/span')
    assert username_error_elem.text == "An account with this username already exists."


def test_registration_password_less_than_8_characters():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    email_input_elem.send_keys("jack@mail.com")
    username_input_elem.send_keys("Jack20")
    password_input_elem.send_keys("Passwd")
    confirm_password_input_elem.send_keys("Passwd")

    register_btn_elem.click()

    time.sleep(2)

    password_error_elem = driver.find_element_by_xpath('//*[@id="register-form-box"]/div[3]/span')
    assert password_error_elem.text == "Password must be at least 8 characters long."

@pytest.mark.django_db
def test_registration_password_and_confirm_password_different():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    email_input_elem.send_keys("jack@mail.com")
    username_input_elem.send_keys("Jack20")
    password_input_elem.send_keys("P@ssw0rd")
    confirm_password_input_elem.send_keys("Password")

    register_btn_elem.click()

    time.sleep(2)

    password_error_elem = driver.find_element_by_xpath('//*[@id="register-form-box"]/div[3]/span')
    assert password_error_elem.text == "Password and Confirm Password do not match."

@pytest.mark.django_db
def test_registration_valid_input():
    # Note: Pytest uses a seperate database that has no records from production application 
    # Delete user if exists in database
    # test_user = User.objects.get(username='Jack20')
    # if test_user is not None:
    #     test_user.delete()


    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    email_input_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    username_input_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_input_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    confirm_password_input_elem = driver.find_element_by_xpath('//*[@id="id_confirm_password"]')
    register_btn_elem = driver.find_element_by_xpath('//*[@id="register-form-btn"]')

    email_input_elem.clear()
    username_input_elem.clear()
    password_input_elem.clear()
    confirm_password_input_elem.clear()

    email_input_elem.send_keys("jack@mail.com")
    username_input_elem.send_keys("Jack20")
    password_input_elem.send_keys("P@ssw0rd")
    confirm_password_input_elem.send_keys("P@ssw0rd")

    register_btn_elem.click()

    time.sleep(2)

    # Assert that latest registered user is the same user that was registered
    # latest_registered_user = User.objects.latest()
    # assert latest_registered_user.get_username() == "Jack20"

    assert driver.title == "Kevin's Blog | Login"

def test_registration_form_click_back():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/account/register")
    login_form_back_btn = driver.find_element_by_xpath('//*[@id="register-form"]/a')
    login_form_back_btn.click()

    time.sleep(2)

    assert driver.title == "Kevin's Blog | Login"