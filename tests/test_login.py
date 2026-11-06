import time
from locators import (
    MainPageLocators, 
    LoginPageLocators, 
    RegisterPageLocators, 
    AccountPageLocators
)

def test_login_from_main_page(driver, registered_user):
    """Вход по кнопке «Войти в аккаунт» на главной."""
    driver.get('https://stellarburgers.education-services.ru/')
    driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
    time.sleep(1)
    
    # Вводим логин и пароль
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    # Принудительно идем в личный кабинет и проверяем кнопку "Выход"
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    assert driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).is_displayed()


def test_login_from_account_button(driver, registered_user):
    """Вход через кнопку «Личный кабинет»."""
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


def test_login_from_register_page(driver, registered_user):
    """Вход через кнопку в форме регистрации."""
    driver.get('https://stellarburgers.education-services.ru/register')
    driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
    time.sleep(1)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    assert driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).is_displayed()


def test_login_from_recovery_page(driver, registered_user):
    """Вход через кнопку в форме восстановления пароля."""
    driver.get('https://stellarburgers.education-services.ru/forgot-password')
    time.sleep(1)
    
    # ВАЖНО: на странице восстановления кнопка "Войти" — это ссылка.
    # Ищем её по тексту, чтобы не промахнуться.
    driver.find_element("xpath", "//a[text()='Войти']").click()
    time.sleep(1)
    
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registered_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registered_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    time.sleep(2)
    
    driver.get('https://stellarburgers.education-services.ru/account')
    time.sleep(1)
    assert driver.find_element(*AccountPageLocators.LOGOUT_BUTTON).is_displayed()