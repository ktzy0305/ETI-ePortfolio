import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from home.models import ContactMessage
import time

def test_access_project_details():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    project_showcase_div_elem = driver.find_element_by_id('projects-showcase')
    driver.execute_script("arguments[0].scrollIntoView(true)", project_showcase_div_elem)
    time.sleep(4)

    project_elem = driver.find_element_by_xpath('//*[@id="projects-showcase"]/div[1]/div/div[1]/div/div[2]/a')
    project_elem.click()
    assert driver.title == "Kevin's Projects | BackToGoal"


def test_contact_form_no_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Scroll the contact form into view or else elements are not interactable
    contact_form_div_elem = driver.find_element_by_id('form-submit')
    driver.execute_script("arguments[0].scrollIntoView(true)", contact_form_div_elem)
    time.sleep(4)

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')

    # Remove the required attributes from the form input tags
    driver.execute_script("arguments[0].removeAttribute('required')", name_elem)
    driver.execute_script("arguments[0].removeAttribute('required')", email_elem)
    driver.execute_script("arguments[0].removeAttribute('required')", message_elem)

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    time.sleep(2)
    submit_btn_elem.click()
    time.sleep(2)

    # Find the error message element and assert value
    message_error_elem = driver.find_element_by_xpath('//*[@id="form-message-textarea"]/p')
    assert message_error_elem.text == "Message cannot be empty!"


def test_contact_form_invalid_email():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Scroll the contact form into view or else elements are not interactable
    contact_form_div_elem = driver.find_element_by_id('form-submit')
    driver.execute_script("arguments[0].scrollIntoView(true)", contact_form_div_elem)
    time.sleep(4)

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')

    # Change the type attribute of email input from email to text to allow invalid email entry.
    driver.execute_script("arguments[0].setAttribute('type','text')", email_elem)

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    name_elem.send_keys("Jack")
    email_elem.send_keys("jack#mail.com")
    message_elem.send_keys("Hi there!")

    time.sleep(2)
    submit_btn_elem.click()

    # Find the error message element and assert value
    email_error_elem = driver.find_element_by_xpath('//*[@id="form-sender-row"]/div[2]/p')
    assert email_error_elem.text == "Invalid email format!"


def test_contact_form_name_more_than_50_characters():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Scroll the contact form into view or else elements are not interactable
    contact_form_div_elem = driver.find_element_by_id('form-submit')
    driver.execute_script("arguments[0].scrollIntoView(true)", contact_form_div_elem)
    time.sleep(4)

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')

    # Change the max length attribute of name input element to 60 to allow input
    driver.execute_script("arguments[0].setAttribute('maxlength','60')", name_elem)

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    username = 'A' * 51

    name_elem.send_keys(username)
    email_elem.send_keys("ray@mail.com")
    message_elem.send_keys("Hi! Would like to meet up?")

    time.sleep(2)
    submit_btn_elem.click()

    # Find the error message element and assert value
    name_error_elem = driver.find_element_by_xpath('//*[@id="form-sender-row"]/div[1]/p')
    assert name_error_elem.text == "Name cannot be longer than 50 characters!"


def test_contact_form_email_more_than_70_characters():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Scroll the contact form into view or else elements are not interactable
    contact_form_div_elem = driver.find_element_by_id('form-submit')
    driver.execute_script("arguments[0].scrollIntoView(true)", contact_form_div_elem)
    time.sleep(4)

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')

    # Change the max length attribute of email input element to 80 to allow input
    driver.execute_script("arguments[0].setAttribute('maxlength','80')", email_elem)

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    email = 'A' * 62

    name_elem.send_keys("Ray")
    email_elem.send_keys("{0}@mail.com".format(email))
    message_elem.send_keys("Hi! Would like to meet up?")

    time.sleep(2)
    submit_btn_elem.click()

    # Find the error message element and assert value
    email_error_elem = driver.find_element_by_xpath('//*[@id="form-sender-row"]/div[2]/p')
    assert email_error_elem.text == "Email cannot be longer than 70 characters!"


def test_contact_form_message_more_than_2000_characters():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Scroll the contact form into view or else elements are not interactable
    contact_form_div_elem = driver.find_element_by_id('form-submit')
    driver.execute_script("arguments[0].scrollIntoView(true)", contact_form_div_elem)
    time.sleep(4)

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')

    # Change the max length attribute of message textarea element to 2000 to allow input
    driver.execute_script("arguments[0].setAttribute('maxlength','2100')", message_elem)

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    message = 'A' * 2001

    name_elem.send_keys("Ray")
    email_elem.send_keys("ray@mail.com")
    message_elem.send_keys(message)

    time.sleep(2)
    submit_btn_elem.click()

    # Find the error message element and assert value
    message_error_elem = driver.find_element_by_xpath('//*[@id="form-message-textarea"]/p')
    assert message_error_elem.text == "Message cannot be longer than 2000 characters!"


@pytest.mark.django_db
def test_contact_form_all_valid_input():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:8000")

    # Scroll the contact form into view or else elements are not interactable
    contact_form_div_elem = driver.find_element_by_id('form-submit')
    driver.execute_script("arguments[0].scrollIntoView(true)", contact_form_div_elem)
    time.sleep(4)

    name_elem = driver.find_element_by_xpath('//*[@id="id_name"]')
    email_elem = driver.find_element_by_xpath('//*[@id="id_email"]')
    message_elem = driver.find_element_by_xpath('//*[@id="id_message"]')
    submit_btn_elem = driver.find_element_by_xpath('//*[@id="form-submit-btn"]')

    name_elem.clear()
    email_elem.clear()
    message_elem.clear()

    name_elem.send_keys("Ray")
    email_elem.send_keys("ray@mail.com")
    message_elem.send_keys("Hi! Would like to meet up?")

    time.sleep(2)
    submit_btn_elem.click()
    time.sleep(3)
    
    # Alternative: Find the modal that pops up if message is successfully sent
    success_modal_title_elem = driver.find_element_by_id('form-submit-ModalLongTitle')


    # Get latest Contact Message from database for assertion
    # Does not work as pytest runs on a seperate database from the actual application

    # Hardcode insert (Uncomment to pass the test case)
    # new_contact_message = ContactMessage(sender_name="Ray", sender_email="ray@mail.com", message="Hi! Would like to meet up?")
    # new_contact_message.save()

    # lastest_contactMessage = ContactMessage.objects.latest("created_on")
    # assert lastest_contactMessage.message == "Hi! Would like to meet up?"
    assert success_modal_title_elem.text == "Success"