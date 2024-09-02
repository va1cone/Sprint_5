import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import time

#проверка перехода по клику на «Личный кабинет».
#def test_the_transition_by_clicking_on_Personal Account
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
driver.find_element(By.XPATH, personal_account_button).click()
time.sleep(2)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'
driver.quit()

#проверка перехода из личного кабинета в «конструктор».
#def test_the_transition_by_clicking_on_conctructor
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
driver.find_element(By.XPATH, personal_account_button).click()
time.sleep(2)
driver.find_element(By.XPATH, button_constructor).click()
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

#проверка перехода при клике на логотип».
#def test_the_transition_when_clicking_on_the_logo
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
driver.find_element(By.XPATH, personal_account_button).click()
time.sleep(2)
driver.find_element(By.XPATH, stellar_burgers_button).click()
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()
