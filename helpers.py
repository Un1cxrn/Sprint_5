import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators
from urls import BASE_URL

def generate_email():
    current_time = int(time.time())
    return f'aleksei_stepanov_57_{current_time}@yandex.ru'

PASSWORD = '123456'
def login(driver, email, password):

    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
    
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
    
    WebDriverWait(driver, 15).until(EC.url_changes(BASE_URL + '/login'))