from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, AccountPageLocators
from urls import BASE_URL, ACCOUNT_PAGE

class TestAccount:
    def login(self, driver, email, password):
        
        WebDriverWait(driver, 15).until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        
        WebDriverWait(driver, 15).until(EC.url_changes(BASE_URL + '/login'))

    def test_go_to_account(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        driver.get(ACCOUNT_PAGE)

        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(AccountPageLocators.LOGOUT_BUTTON)
        ).is_displayed()

    def test_go_to_constructor_from_account(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        driver.get(ACCOUNT_PAGE)
        
        constructor_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(AccountPageLocators.CONSTRUCTOR_BUTTON))
        driver.execute_script("arguments[0].click();", constructor_btn)
        

        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.ACCOUNT_BUTTON)
        ).is_displayed()

    def test_go_to_constructor_by_logo(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        driver.get(ACCOUNT_PAGE)
        

        logo = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(AccountPageLocators.LOGO))
        driver.execute_script("arguments[0].click();", logo)
        
        assert WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(MainPageLocators.ACCOUNT_BUTTON)
        ).is_displayed()

    def test_logout(self, driver, registered_user):
        driver.get(BASE_URL)
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        
        self.login(driver, registered_user["email"], registered_user["password"])
        
        driver.get(ACCOUNT_PAGE)
        
        logout_btn = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON))
        driver.execute_script("arguments[0].click();", logout_btn)
        
        assert WebDriverWait(driver, 15).until(EC.url_contains('/login'))