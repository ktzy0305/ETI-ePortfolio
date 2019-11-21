import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_blog_details_comment_user_not_logged_in():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/1/")
    login_hyperlink_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div/div/a')
    assert login_hyperlink_elem == "Login"

def test_blog_details_comment_user_is_logged_in():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/1/")
    login_hyperlink_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div/div/a')
    login_hyperlink_elem.click()
    
    time.sleep(2)

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("David3k")
    password_elem.send_keys("Cyan30red")

    login_btn_elem.click()

    time.sleep(2)

    comment_header_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div[2]/h3[1]')
    assert comment_header_elem.text == "Leave a comment:"

def test_blog_details_comment_no_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/1/")
    login_hyperlink_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div/div/a')
    login_hyperlink_elem.click()
    
    time.sleep(2)

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("David3k")
    password_elem.send_keys("Cyan30red")

    login_btn_elem.click()

    time.sleep(2)

    comment_text_area_elem = driver.find_element_by_xpath('//*[@id="id_body"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div[2]/form/button')
    comment_text_area_elem.clear()
    submit_btn_elem.click()

    # Assert is error found
    return

def test_blog_details_comment_valid_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/1/")
    login_hyperlink_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div/div/a')
    login_hyperlink_elem.click()
    
    time.sleep(2)

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("David3k")
    password_elem.send_keys("Cyan30red")

    login_btn_elem.click()

    time.sleep(2)

    comment_text_area_elem = driver.find_element_by_xpath('//*[@id="id_body"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div[2]/form/button')
    comment_text_area_elem.clear()
    comment_text_area_elem.send_keys("This project looks good.")
    submit_btn_elem.click()

    time.sleep(2)

    recent_comment_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div[2]/p[5]')
    assert recent_comment_elem.text == "This project looks good."

def test_blog_details_comment_input_more_than_2000_characters():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/1/")
    login_hyperlink_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div/div/a')
    login_hyperlink_elem.click()
    
    time.sleep(2)

    username_elem = driver.find_element_by_xpath('//*[@id="id_username"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    login_btn_elem = driver.find_element_by_xpath('//*[@id="login-form-btn"]')

    username_elem.clear()
    password_elem.clear()

    username_elem.send_keys("David3k")
    password_elem.send_keys("Cyan30red")

    login_btn_elem.click()

    time.sleep(2)

    comment_text_area_elem = driver.find_element_by_xpath('//*[@id="id_body"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="blog-detail-container"]/div[2]/form/button')
    comment_text_area_elem.clear()
    long_text = "i" * 2001
    comment_text_area_elem.send_keys(long_text)
    submit_btn_elem.click()

    
    # Assert if error label is shown
    return