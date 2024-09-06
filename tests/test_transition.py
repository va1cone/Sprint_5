from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import *
from conftest import *

class TestTransition:
    def test_the_transition_by_clicking_on_personal_account(self, start_driver):
        driver = start_driver
        driver.get(login_page)
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, personal_account_button)))
        driver.find_element(By.XPATH, personal_account_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((profile_page)))
        assert driver.current_url == profile_page

    def test_the_transition_by_clicking_on_conctructor(self, start_driver):
        driver = start_driver
        driver.get(login_page)

        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, personal_account_button)))
        driver.find_element(By.XPATH, personal_account_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, button_constructor)))
        driver.find_element(By.XPATH, button_constructor).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((home_page)))
        assert driver.current_url == home_page
    def test_the_transition_when_clicking_on_the_logo(self, start_driver):
        driver = start_driver
        driver.get(login_page)
        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, personal_account_button)))
        driver.find_element(By.XPATH, personal_account_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.element_to_be_clickable((By.XPATH, stellar_burgers_button)))
        driver.find_element(By.XPATH, stellar_burgers_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((home_page)))
        assert driver.current_url == home_page
