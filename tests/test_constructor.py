from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators
from urls import BASE_URL

class TestConstruction:
    def test_buns_tab(self,driver):

        driver.get(BASE_URL)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPageLocators.BUNS_TAB))
        driver.execute_script("arguments[0].click();", button)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.BUNS_TAB_ACTIVE)
        )
        assert driver.find_element(*ConstructorPageLocators.BUNS_TAB_ACTIVE).is_displayed()

    def test_sauces_tab(self,driver):

        driver.get(BASE_URL)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPageLocators.SAUCES_TAB))
        driver.execute_script("arguments[0].click();", button)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.SAUCES_TAB_ACTIVE)
        )
        assert driver.find_element(*ConstructorPageLocators.SAUCES_TAB_ACTIVE).is_displayed()

    def test_fillings_tab(self,driver):

        driver.get(BASE_URL)
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(ConstructorPageLocators.FILLINGS_TAB))
        driver.execute_script("arguments[0].click();", button)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(ConstructorPageLocators.FILLINGS_TAB_ACTIVE)
        )
        assert driver.find_element(*ConstructorPageLocators.FILLINGS_TAB_ACTIVE).is_displayed()