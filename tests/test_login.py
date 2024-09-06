from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import *
from conftest import *

class TestLogin:
    def test_login_after_registration(self, start_driver):
        driver = start_driver
        driver.get(registration_page)

        driver.find_element(By.XPATH, registration_name_entry_field).send_keys('valeria')
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
        driver.find_element(By.XPATH, register_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((login_page)))
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(new_email)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys('qwerty123')
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, collect_burger_text)))
        assert collect_burger_text

    def test_using_the_log_in_to_your_account(self, start_driver):
        driver = start_driver
        driver.get(home_page)

        driver.find_element(By.XPATH, login_button_on_the_main_page).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((login_page)))
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        driver.find_element(By.XPATH, login_button).click()
        assert collect_burger_text

    def test_login_via_personal_account(self, start_driver):
        driver = start_driver
        driver.get(registration_page)
        driver.find_element(By.XPATH, personal_account_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, registration_email_entry_field)))
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((home_page)))
        assert driver.current_url == home_page

    def test_login_via_the_button_in_the_password_recovery_form(self, start_driver):
        driver = start_driver
        driver.get(login_page)

        driver.find_element(By.XPATH, recover_password_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, Login_button_when_recovering_password)))
        driver.find_element(By.XPATH, Login_button_when_recovering_password).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((login_page)))
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((home_page)))
        assert driver.current_url == home_page