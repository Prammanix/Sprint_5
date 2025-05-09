from selenium.webdriver.common.by import By

# Локаторы страницы регистрации
NAME_INPUT = (By.XPATH, '//input[@placeholder="Имя"]')
EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Email"]')
PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Пароль"]')
REGISTER_BUTTON = (By.XPATH, '//button[contains(text(),"Зарегистрироваться")]')
ERROR_MESSAGE = (By.XPATH, '//p[contains(text(),"Такой пользователь уже существует")]')

# Локаторы страницы входа
LOGIN_ACCOUNT_BUTTON = (By.XPATH, '//button[contains(text(),"Войти в аккаунт")]')
PERSONAL_CABINET_BUTTON = (By.XPATH, '//header//nav//a[@href="/account"]')
REGISTER_FORM_LOGIN_BUTTON = (By.XPATH, '//a[contains(text(), "Войти")]')
FORGOT_PASSWORD_LOGIN_BUTTON = (By.XPATH, '//a[contains(text(), "Войти")]')

# Локаторы личного кабинета и переходов
LOGOUT_BUTTON = (By.XPATH, '//button[text()="Выход"]')
CONSTRUCTOR_BUTTON = (By.XPATH, '//header//nav//a[@href="/"]')

# Локаторы разделов в конструкторе
BUNS_SECTION = (By.XPATH, '//div[contains(@class, "tab") and contains(text(), "Булки")]')
SAUCES_SECTION = (By.XPATH, '//div[contains(@class, "tab") and contains(text(), "Соусы")]')
FILLINGS_SECTION = (By.XPATH, '//div[contains(@class, "tab") and contains(text(), "Начинки")]')

# Локаторы контента внутри разделов
BUNS_CONTENT = (By.XPATH, '//div[contains(@class, "content") and contains(text(), "Булки")]')
SAUCES_CONTENT = (By.XPATH, '//div[contains(@class, "content") and contains(text(), "Соусы")]')
FILLINGS_CONTENT = (By.XPATH, '//div[contains(@class, "content") and contains(text(), "Начинки")]')

