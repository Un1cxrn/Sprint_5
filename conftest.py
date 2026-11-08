import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators
from helpers import generate_email, PASSWORD
from urls import REGISTER_PAGE

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def registered_user(driver):
    email = generate_email()
    password = PASSWORD
    
    driver.get(REGISTER_PAGE)
    
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Булка')
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    
    WebDriverWait(driver, 10).until(
        EC.url_contains('/login')
    )
    
    return {"email": email, "password": PASSWORD}