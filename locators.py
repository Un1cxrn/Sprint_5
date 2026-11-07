from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Поле ввода Email на странице входа
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
    # Поле ввода пароля на странице входа
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")


class RegisterPageLocators:
    # Поле ввода имени при регистрации
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    # Поле ввода Email при регистрации
    EMAIL_INPUT = (By.XPATH, "(//input[@name='name'])[2]")
    # Поле ввода пароля при регистрации
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")
    # Ссылка "Войти"
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class MainPageLocators:
    # Кнопка "Личный кабинет" в шапке сайта
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")


class RecoveryPageLocators:
    # Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class AccountPageLocators:
    # Кнопка "Конструктор" на странице личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип в шапке
    LOGO = (By.XPATH, '//header//a')
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class ConstructorPageLocators:
    # Вкладка "Булки"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    # Вкладка "Соусы"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    # Вкладка "Начинки"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    
    # Активная вкладка "Булки" (добавляется класс tab_tab_type_current)
    BUNS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
    # Активная вкладка "Соусы"
    SAUCES_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
    # Активная вкладка "Начинки"
    FILLINGS_TAB_ACTIVE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")