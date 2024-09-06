from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import *
from conftest import *

class TestConstructor:
    def test_the_transition_to_the_sauces_section(self, start_driver):
        driver = start_driver
        driver.get(login_page)

        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, sauces_button)))
        driver.find_element(By.XPATH, sauces_button).click()
        sauces_element = driver.find_element(By.XPATH, sauces_button)
        assert 'current' in sauces_element.get_attribute('class')
    def test_the_transition_to_the_buns_section(self, start_driver):
        driver = start_driver
        driver.get(login_page)

        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(expected_conditions.element_to_be_clickable((By.XPATH, sauces_button)))
        driver.find_element(By.XPATH, sauces_button).click()
        driver.find_element(By.XPATH, bun_button).click()
        buns_element = driver.find_element(By.XPATH, bun_button)
        assert 'current' in buns_element.get_attribute('class')
    def test_the_transition_to_the_stuffings_section(self, start_driver):
        driver = start_driver
        driver.get(login_page)

        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, stuffing_button)))
        driver.find_element(By.XPATH, stuffing_button).click()
        stuffings_element = driver.find_element(By.XPATH, stuffing_button)
        assert 'current' in stuffings_element.get_attribute('class')

