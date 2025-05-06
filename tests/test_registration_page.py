import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestRegistration(unittest.TestCase):

    def test_successful_registration(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/register")

            # Заполнение поля "Имя" уникальным значением
            name_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')
            name_input.send_keys("Тестовое Имя Уникальное")

            # Уникальный email с timestamp
            email_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input')
            email_input.send_keys(f"unique_{int(time.time())}@ya.ru")

            # Пароль 6 символов
            password_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/div/input')
            password_input.send_keys("123456")

            # Кнопка регистрации
            register_button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button')
            register_button.click()

            time.sleep(2)

            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/login")
        finally:
            driver.quit()

    def test_registration_existing_user(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/register")

            # Имя пользователя
            name_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[1]/div/div/input')
            name_input.send_keys("Тестовое Имя")

            # Существующий email
            email_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[2]/div/div/input')
            email_input.send_keys("123@ya.ru")

            # Пароль
            password_input = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/fieldset[3]/div/div/input')
            password_input.send_keys("123456")

            # Кнопка регистрации
            register_button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/form/button')
            register_button.click()

            time.sleep(2)

            error_message = driver.find_element(By.XPATH, '/html/body/div/div/main/div/p')
            self.assertTrue(error_message.is_displayed())
            self.assertEqual(error_message.text, "Такой пользователь уже существует")
        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()
