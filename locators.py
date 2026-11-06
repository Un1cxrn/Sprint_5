from selenium.webdriver.common.by import By


class LoginPageLocators:
    # Поле ввода Email на странице входа
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    # Поле ввода пароля на странице входа
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    # Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a')


class RegisterPageLocators:
    # Поле ввода имени при регистрации
    NAME_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input')
    # Поле ввода Email при регистрации (ДОБАВИЛИ /input в конец!)
    EMAIL_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input')
    # Поле ввода пароля при регистрации
    PASSWORD_INPUT = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input')
    # Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')
    # Сообщение об ошибке (Некорректный пароль)
    ERROR_MESSAGE = (By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p')
    # Ссылка на страницу входа
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button')
    # Кнопка "Личный Кабинет" в шапке сайта
    ACCOUNT_BUTTON = (By.XPATH, '//*[@id="root"]/div/header/nav/a/p')


class RecoveryPageLocators:
    # Кнопка "Восстановить" на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, '//*[@id="root"]/div/main/div/form/button')


class AccountPageLocators:
    # Кнопка "Конструктор" на странице личного кабинета
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип в шапке
    LOGO = (By.XPATH, '//header//a')
    # Кнопка "Выход"
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class ConstructorPageLocators:
    # Вкладка "Булки"
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    # Вкладка "Соусы"
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    # Вкладка "Начинки"
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    
    # Заголовок раздела "Булки"
    BUNS_SECTION = (By.XPATH, "//h2[text()='Булки']")
    # Заголовок раздела "Соусы"
    SAUCES_SECTION = (By.XPATH, "//h2[text()='Соусы']")
    # Заголовок раздела "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//h2[text()='Начинки']")