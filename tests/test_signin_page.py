import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin(unittest.TestCase):

    def test_login_via_account_button(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            login_button = driver.find_element(By.XPATH, '/html/body/div/div/main/section[2]/div/button')
            login_button.click()
            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/login")
        finally:
            driver.quit()

    def test_login_via_personal_cabinet_button(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/")
            personal_cabinet_button = driver.find_element(By.XPATH, '/html/body/div/div/header/nav/a')
            personal_cabinet_button.click()
            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/login")
        finally:
            driver.quit()

    def test_login_via_registration_form(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/register")
            login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
            login_button.click()
            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/login")
        finally:
            driver.quit()

    def test_login_via_forgot_password_form(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        try:
            driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
            login_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div/div/p/a')
            login_button.click()
            self.assertEqual(driver.current_url, "https://stellarburgers.nomoreparties.site/login")
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()