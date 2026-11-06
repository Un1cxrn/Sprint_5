import time
from locators import MainPageLocators, LoginPageLocators, AccountPageLocators

def test_go_to_account(driver, registered_user):
    """Переход в личный кабинет по клику."""
    driver.get('https://stellarburgers.education-services.ru/')
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
    time.sleep(1)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    assert driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).is_displayed()

def test_go_to_constructor_from_account(driver, registered_user):
    """Переход из личного кабинета в конструктор по кнопке."""
    driver.get('https://stellarburgers.education-services.ru/')
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
    time.sleep(1)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    
    driver.find_element(*AccountPageLocators.CONSTRUCTOR_BUTTON).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.education-services.ru/'

def test_go_to_constructor_by_logo(driver, registered_user):
    """Переход из личного кабинета в конструктор по логотипу."""
    driver.get('https://stellarburgers.education-services.ru/')
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
    time.sleep(1)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    
    driver.find_element(*AccountPageLocators.LOGO).click()
    time.sleep(1)
    assert driver.current_url == 'https://stellarburgers.education-services.ru/'

def test_logout(driver, registered_user):
    """Проверка выхода из аккаунта."""
    driver.get('https://stellarburgers.education-services.ru/')
    driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
    time.sleep(1)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    
    driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).click()
    time.sleep(1)
    assert 'login' in driver.current_url