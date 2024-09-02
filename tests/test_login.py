import random
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import time

#вход после регистрации
#def test_login_after_registration():
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
assert button_place_an_order
driver.quit()

#вход по кнопке «Войти в аккаунт» на главной
#def test_using_the_Log_in_to_your_account():
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
driver.find_element(By.XPATH, personal_account_button).click()
time.sleep(5)
driver.find_element(By.XPATH, exit_button).click()
time.sleep(5)
driver.find_element(By.XPATH, stellar_burgers_button).click()
time.sleep(5)
driver.find_element(By.XPATH, login_button_on_the_main_page).click()
time.sleep(5)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, login_button).click()
assert button_place_an_order
driver.quit()

#вход через личный кабинет
#def login_via_personal_account:
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
driver.find_element(By.XPATH, personal_account_button).click()
time.sleep(5)
driver.find_element(By.XPATH, exit_button).click()
time.sleep(5)
driver.find_element(By.XPATH, stellar_burgers_button).click()
time.sleep(5)
driver.find_element(By.XPATH, personal_account_button).click()
time.sleep(5)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, login_button).click()
time.sleep(5)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

#вход через кнопку в форме восстановления пароля
#def login_via_the_button_in_the_password_recovery_form():
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
driver.find_element(By.XPATH, exit_button).click()
time.sleep(2)
driver.find_element(By.XPATH, recover_password_button).click()
time.sleep(2)
driver.find_element(By.XPATH, Login_button_when_recovering_password).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
time.sleep(2)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()