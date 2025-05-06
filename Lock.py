# Регистрация:
NAME_INPUT_XPATH = '/html/body/div/div/main/div/form/fieldset[1]/div/div/input'  # input для ввода имени пользователя
EMAIL_INPUT_XPATH = '/html/body/div/div/main/div/form/fieldset[2]/div/div/input'  # input для ввода email
PASSWORD_INPUT_XPATH = '/html/body/div/div/main/div/form/fieldset[3]/div/div/input'  # input для ввода пароля
REGISTER_BUTTON_XPATH = '/html/body/div/div/main/div/form/button'  # кнопка "Зарегистрироваться"
ERROR_MESSAGE_XPATH = '/html/body/div/div/main/div/p'  # абзац с текстом ошибки "Такой пользователь уже существует"

# Вход:
LOGIN_ACCOUNT_BUTTON_XPATH = '/html/body/div/div/main/section[2]/div/button'  # кнопка "Войти в аккаунт" на главной
PERSONAL_CABINET_BUTTON_XPATH = '/html/body/div/div/header/nav/a'  # кнопка "Личный кабинет" в шапке сайта
REGISTER_FORM_LOGIN_BUTTON_XPATH = '//*[@id="root"]/div/main/div/div/p/a'  # ссылка "Войти" в форме регистрации
FORGOT_PASSWORD_LOGIN_BUTTON_XPATH = '//*[@id="root"]/div/main/div/div/p/a'  # ссылка "Войти" в форме восстановления пароля

# Переходы и личный кабинет:
PERSONAL_CABINET_MENU_XPATH = '/html/body/div/div/header/nav/a/p'  # <p> "Личный Кабинет" в шапке сайта
CONSTRUCTOR_BUTTON_XPATH = '/html/body/div/div/header/nav/ul/li[1]/a'  # ссылка "Конструктор" с иконкой и текстом
LOGOUT_BUTTON_XPATH = '/html/body/div/div/main/div/nav/ul/li[3]/button'  # кнопка "Выход" из аккаунта

# Разделы конструктора:
BUNS_SECTION_XPATH = '/html/body/div/div/main/section[1]/div[1]/div[1]'  # селектор раздела "Булки"
SAUCES_SECTION_XPATH = '/html/body/div/div/main/section[1]/div[1]/div[2]'  # селектор раздела "Соусы"
FILLINGS_SECTION_XPATH = '/html/body/div/div/main/section[1]/div[1]/div[3]'  # селектор раздела "Начинки"
