import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from home.models import ContactMessage
import time

def test_access_project_details():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")
    project_elem = driver.find_element_by_xpath('//*[@id="projects-showcase"]/div[1]/div/div[1]/div/div[2]/a')
    actions = ActionChains(driver)
    actions.move_to_element(project_elem).perform()
    project_elem.click()
    assert driver.title == "Kevin's Project | BackToGoal"


def test_contact_form_no_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')
    footer_elem = driver.find_element_by_xpath('//*[@id="contact-footer"]')

    actions = ActionChains(driver)
    actions.move_to_element(submit_btn_elem).perform()

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    time.sleep(5)
    submit_btn_elem.click()
    driver.implicitly_wait(5)

    message_error_elem = driver.find_element_by_xpath('//*[@id="form-message-textarea"]/p')
    assert message_error_elem == "Message cannot be empty!"

def test_contact_form_invalid_email():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')
    footer_elem = driver.find_element_by_xpath('//*[@id="contact-footer"]')

    actions = ActionChains(driver)
    actions.move_to_element(submit_btn_elem).perform()

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    name_elem.send_keys("Jack")
    email_elem.send_keys("jack#mail.com")
    message_elem.send_keys("Hi there!")

    time.sleep(5)
    submit_btn_elem.click()
    driver.implicitly_wait(5)

    email_error_elem = driver.find_element_by_xpath('//*[@id="form-sender-row"]/div[2]/p')
    assert email_error_elem.text == "Invalid email format!"


@pytest.mark.django_db
def test_contact_form_all_valid_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")
    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')
    footer_elem = driver.find_element_by_xpath('//*[@id="contact-footer"]')

    actions = ActionChains(driver)
    actions.move_to_element(submit_btn_elem).perform()

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    name_elem.send_keys("Ray")
    email_elem.send_keys("ray222@mail.com")
    message_elem.send_keys("Hi! Would like to meet up?")

    time.sleep(5)
    submit_btn_elem.click()
    driver.implicitly_wait(5)
    lastest_contactMessage = ContactMessage.objects.get(pk=ContactMessage.objects.all().count())
    assert lastest_contactMessage.message == "Hi! Would like to meet up?"
    

    return