from selenium import webdriver
import pytest

@pytest.fixture
def start_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()