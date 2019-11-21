import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_click_blog_post_title_at_blog_category():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000/blog/Personal%20Project/")
    blog_post_title_elem = driver.find_element_by_xpath('//*[@id="blog-category-container"]/div/h2/a')
    blog_post_title_elem.click()
    assert driver.title == "Kevin's Blog | Shopify"