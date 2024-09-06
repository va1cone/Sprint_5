from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import *
from helpers import *
from conftest import *

class TestLogoutFromAccount:
    def test_the_logout(self, start_driver):
        driver = start_driver
        driver.get(login_page)

        driver.find_element(By.XPATH, registration_email_entry_field).send_keys(test_login)
        driver.find_element(By.NAME, registration_password_entry_field).send_keys(test_password)
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, login_button)))
        driver.find_element(By.XPATH, login_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, personal_account_button)))
        driver.find_element(By.XPATH, personal_account_button).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, exit_button)))
        driver.find_element(By.XPATH, exit_button).click()
        WebDriverWait(driver, 2).until(
            expected_conditions.url_to_be((login_page)))
        assert driver.current_url == login_page
        driver.quit()