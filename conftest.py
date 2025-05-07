import datetime
import logging

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_login_email():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    email = f"user_{timestamp}@example.com"
    logging.info(f"Сгенерирован логин: {email}")  # Логирование сгенерированного email
    return email

# Пример использования
login_email = generate_login_email()
