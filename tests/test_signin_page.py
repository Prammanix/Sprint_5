import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_BUTTON, PERSONAL_CABINET_BUTTON, REGISTRATION_LOGIN_BUTTON, FORGOT_PASSWORD_LOGIN_BUTTON

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_login_via_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_personal_cabinet_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*PERSONAL_CABINET_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_registration_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*REGISTRATION_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_login_via_forgot_password_form(driver):
    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(*FORGOT_PASSWORD_LOGIN_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
