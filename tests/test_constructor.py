import time
from locators import ConstructorPageLocators

def test_buns_tab(driver):
    """Проверка вкладки «Булки»."""
    driver.get('https://stellarburgers.education-services.ru/')
    time.sleep(1)
    
    # Используем JavaScript-клик, чтобы обойти перекрытия
    button = driver.find_element(*ConstructorPageLocators.BUNS_TAB)
    driver.execute_script("arguments[0].click();", button)
    
    time.sleep(1)
    assert driver.find_element(*ConstructorPageLocators.BUNS_SECTION).is_displayed()

def test_sauces_tab(driver):
    """Проверка вкладки «Соусы»."""
    driver.get('https://stellarburgers.education-services.ru/')
    time.sleep(1)
    
    button = driver.find_element(*ConstructorPageLocators.SAUCES_TAB)
    driver.execute_script("arguments[0].click();", button)
    
    time.sleep(1)
    assert driver.find_element(*ConstructorPageLocators.SAUCES_SECTION).is_displayed()

def test_fillings_tab(driver):
    """Проверка вкладки «Начинки»."""
    driver.get('https://stellarburgers.education-services.ru/')
    time.sleep(1)
    
    button = driver.find_element(*ConstructorPageLocators.FILLINGS_TAB)
    driver.execute_script("arguments[0].click();", button)
    
    time.sleep(1)
    assert driver.find_element(*ConstructorPageLocators.FILLINGS_SECTION).is_displayed()