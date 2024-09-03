from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import time

#вход после регистрации
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, button_place_an_order)))
assert button_place_an_order
driver.quit()

#вход по кнопке «Войти в аккаунт» на главной
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email2)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email2)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
driver.find_element(By.XPATH, personal_account_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, exit_button)))
driver.find_element(By.XPATH, exit_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, stellar_burgers_button)))
driver.find_element(By.XPATH, stellar_burgers_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button_on_the_main_page)))
driver.find_element(By.XPATH, login_button_on_the_main_page).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email2)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, login_button).click()
assert button_place_an_order
driver.quit()

#вход через личный кабинет
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email3)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email3)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
driver.find_element(By.XPATH, personal_account_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, exit_button)))
driver.find_element(By.XPATH, exit_button).click()
time.sleep(2)
driver.find_element(By.XPATH, stellar_burgers_button).click()
time.sleep(2)
driver.find_element(By.XPATH, personal_account_button).click()
WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH,registration_email_entry_field)))
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email3)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, login_button).click()
time.sleep(2)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()

#вход через кнопку в форме восстановления пароля
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email4)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email4)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, personal_account_button)))
driver.find_element(By.XPATH, personal_account_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, exit_button)))
driver.find_element(By.XPATH, exit_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, recover_password_button)))
driver.find_element(By.XPATH, recover_password_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, Login_button_when_recovering_password)))
driver.find_element(By.XPATH, Login_button_when_recovering_password).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email4)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, login_button).click()
time.sleep(2)
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
driver.quit()