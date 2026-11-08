from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RegisterPageLocators, AccountPageLocators
from urls import BASE_URL, REGISTER_PAGE, FORGOT_PASSWORD_PAGE
from helpers import login 

class TestLogin:
    def test_login_from_main_page(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        
        login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_login_from_account_button(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        
        login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_login_from_register_page(self, driver, registered_user):
        driver.get(REGISTER_PAGE)
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        
        login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_login_from_recovery_page(self, driver, registered_user):
        driver.get(FORGOT_PASSWORD_PAGE)
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Войти']"))
        ).click()
        
        login(driver, registered_user["email"], registered_user["password"])
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_BUTTON)).click()
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()