import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NAME_INPUT, EMAIL_INPUT, PASSWORD_INPUT, REGISTER_BUTTON, ERROR_MESSAGE
from utils import generate_login_email

@pytest.fixture
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*NAME_INPUT).send_keys("Тестовое Имя Уникальное")
    driver.find_element(*EMAIL_INPUT).send_keys(generate_login_email())
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_registration_existing_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    driver.find_element(*NAME_INPUT).send_keys("Тестовое Имя")
    driver.find_element(*EMAIL_INPUT).send_keys("123@ya.ru")
    driver.find_element(*PASSWORD_INPUT).send_keys("123456")
    driver.find_element(*REGISTER_BUTTON).click()

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(ERROR_MESSAGE)
    )
    assert error_message.is_displayed()
    assert error_message.text == "Такой пользователь уже существует"

