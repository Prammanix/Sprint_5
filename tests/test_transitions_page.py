import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAccount(unittest.TestCase):

    def test_transition_to_personal_cabinet(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")

            # Нажимаем кнопку "Личный кабинет"
            personal_cabinet_button = driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a/p')
            personal_cabinet_button.click()

            time.sleep(2)  # Ждем загрузки страницы
            self.assertIn("account/profile", driver.current_url)
        finally:
            driver.quit()

    def test_transition_from_personal_cabinet_to_constructor(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/account/profile")

            # Нажимаем кнопку "Конструктор"
            constructor_button = driver.find_element(By.XPATH, '/html/body/div/div/header/nav/ul/li[1]/a')
            constructor_button.click()

            time.sleep(2)
            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/")
        finally:
            driver.quit()

    def test_logout(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/account/profile")

            # Нажимаем кнопку "Выход"
            logout_button = driver.find_element(By.XPATH, '/html/body/div/div/main/div/nav/ul/li[3]/button')
            logout_button.click()

            time.sleep(2)
            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/login")
        finally:
            driver.quit()

    def test_transition_to_buns_section(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")

            # Нажимаем на раздел "Булки"
            buns_section = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[1]')
            buns_section.click()

            time.sleep(2)
            content = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[2]')
            self.assertIn("Булки", content.text)
        finally:
            driver.quit()

    def test_transition_to_sauces_section(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")

            # Нажимаем на раздел "Соусы"
            sauces_section = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[2]')
            sauces_section.click()

            time.sleep(2)
            content = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[2]')
            self.assertIn("Соусы", content.text)
        finally:
            driver.quit()

    def test_transition_to_fillings_section(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")

            # Нажимаем на раздел "Начинки"
            fillings_section = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[1]/div[3]')
            fillings_section.click()

            time.sleep(2)
            content = driver.find_element(By.XPATH, '/html/body/div/div/main/section[1]/div[2]')
            self.assertIn("Начинки", content.text)
        finally:
            driver.quit()


if __name__ == "__main__":
    unittest.main()