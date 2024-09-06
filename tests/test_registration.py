from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import *
from conftest import *

class TestRegistration:

    def test_registration_with_correct_data(self, start_driver):
        driver = start_driver
        driver.get(registration_page)

        driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')

        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((login_page)))
        assert driver.current_url == login_page

    def test_registration_with_not_correct_password(self, start_driver):
        driver = start_driver
        driver.get(registration_page)
        driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email2)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys('q')
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, text_incorrect_password)))
        assert text_incorrect_password


