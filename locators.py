from selenium.webdriver.common.by import By

# Локаторы для тестов регистрации
NAME_INPUT = (By.XPATH, '//input[@placeholder="Имя"]')
EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Email"]')
PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Пароль"]')
REGISTER_BUTTON = (By.XPATH, '//button[text()="Зарегистрироваться"]')
ERROR_MESSAGE = (By.XPATH, '//p[contains(text(), "Такой пользователь уже существует")]')

# Локаторы для тестов входа
LOGIN_ACCOUNT_BUTTON = (By.XPATH, '/html/body/div/div/main/section[2]/div/button')
PERSONAL_CABINET_BUTTON = (By.XPATH, '/html/body/div/div/header/nav/a')
REGISTER_FORM_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
FORGOT_PASSWORD_LOGIN_BUTTON = (By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')

# Локаторы для тестов аккаунта и переходов
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
BUNS_SECTION = (By.XPATH, '//div[contains(@class, "tab") and contains(text(), "Булки")]')
SAUCES_SECTION = (By.XPATH, '//div[contains(@class, "tab") and contains(text(), "Соусы")]')
FILLINGS_SECTION = (By.XPATH, '//div[contains(@class, "tab") and contains(text(), "Начинки")]')
CONSTRUCTOR_BUTTON = (By.XPATH, '//a[contains(@href, "/")]')
PERSONAL_CABINET_MENU = (By.XPATH, '//p[contains(text(), "Личный Кабинет")]')
