# test_signin_page.py
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_ACCOUNT_BUTTON, PERSONAL_CABINET_BUTTON, REGISTER_FORM_LOGIN_BUTTON, FORGOT_PASSWORD_LOGIN_BUTTON

@pytest.fixture(scope="function")
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_via_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_personal_cabinet_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_registration_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*REGISTER_FORM_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_forgot_password_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*FORGOT_PASSWORD_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
