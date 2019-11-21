import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_click_blog_post_title_at_blog_index():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/")
    blog_post_title_elem = driver.find_element_by_xpath('//*[@id="blog-index-container"]/div[1]/h2/a')
    blog_post_title_elem.click()
    assert driver.title == "Kevin's Blog | Cycling Journey: Changi towards the City"

def test_click_blog_post_category():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/")
    blog_post_category = driver.find_element_by_xpath('//*[@id="blog-index-container"]/div[2]/small/a')
    blog_post_category.click()
    assert driver.title == "Kevin's Blog | Category: School Project"