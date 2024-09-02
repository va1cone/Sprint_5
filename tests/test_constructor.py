import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import time

#проверка перехода к разделу "соусы"
#def test_the_transition_to_the_sauces_section():
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
time.sleep(2)
driver.find_element(By.XPATH, login_button).click()
time.sleep(5)
driver.find_element(By.XPATH, sauces_button).click()
time.sleep(2)
sauces_element = driver.find_element(By.XPATH, sauces_button)
assert 'current' in sauces_element.get_attribute('class')

#проверка перехода к разделу "булки"
#def test_the_transition_to_the_buns_section():
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
time.sleep(2)
driver.find_element(By.XPATH, login_button).click()
time.sleep(5)
driver.find_element(By.XPATH, sauces_button).click()
time.sleep(2)
driver.find_element(By.XPATH, bun_button).click()
buns_element = driver.find_element(By.XPATH, bun_button)
assert 'current' in buns_element.get_attribute('class')

#проверка перехода к разделу "начинки"
#def test_the_transition_to_the_stuffings_section():
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
time.sleep(2)
driver.find_element(By.XPATH, login_button).click()
time.sleep(2)
driver.find_element(By.XPATH, stuffing_button).click()
stuffings_element = driver.find_element(By.XPATH, stuffing_button)
time.sleep(2)
assert 'current' in stuffings_element.get_attribute('class')

