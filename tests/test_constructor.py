from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
import time

#проверка перехода к разделу "соусы"
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, sauces_button)))
driver.find_element(By.XPATH, sauces_button).click()
time.sleep(2)
sauces_element = driver.find_element(By.XPATH, sauces_button)
assert 'current' in sauces_element.get_attribute('class')
driver.quit()

#проверка перехода к разделу "булки"
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email2)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email2)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, sauces_button)))
driver.find_element(By.XPATH, sauces_button).click()
time.sleep(2)
driver.find_element(By.XPATH, bun_button).click()
time.sleep(2)
buns_element = driver.find_element(By.XPATH, bun_button)
assert 'current' in buns_element.get_attribute('class')
driver.quit()

#проверка перехода к разделу "начинки"
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/register")

driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email3)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
driver.find_element(By.XPATH, register_button).click()
time.sleep(2)
driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email3)
driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
driver.find_element(By.XPATH, login_button).click()
WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, stuffing_button)))
driver.find_element(By.XPATH, stuffing_button).click()
time.sleep(2)
stuffings_element = driver.find_element(By.XPATH, stuffing_button)
assert 'current' in stuffings_element.get_attribute('class')
driver.quit()

