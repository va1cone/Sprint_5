from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import time
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
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
driver.quit()