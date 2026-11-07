from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    MainPageLocators, LoginPageLocators, RegisterPageLocators, AccountPageLocators
)
from urls import BASE_URL, REGISTER_PAGE, FORGOT_PASSWORD_PAGE

class TestLogin:
    def login(self, driver, email, password):
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def test_login_from_main_page(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_login_from_account_button(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_login_from_register_page(self, driver, registered_user):
        driver.get(REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_login_from_recovery_page(self, driver, registered_user):
        driver.get(FORGOT_PASSWORD_PAGE)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        ).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()