from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegisterPageLocators, LoginPageLocators
from helpers import generate_email, PASSWORD
from urls import REGISTER_PAGE

def test_successful_registration(driver):
    email = generate_email()
    
    driver.get(REGISTER_PAGE)
    
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Булка')
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(PASSWORD)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    
    assert WebDriverWait(driver, 15).until(
        EC.url_contains('/login')
    )

def test_registration_with_short_pwd(driver):
    email = generate_email()
    short_password = '12345' 
    
    driver.get(REGISTER_PAGE)
    
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Булка')
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(short_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    
    error_message = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located(RegisterPageLocators.ERROR_MESSAGE)
    )
    assert error_message.text == 'Некорректный пароль'