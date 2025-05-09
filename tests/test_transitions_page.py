# test_transitions_page.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGOUT_BUTTON, BUNS_SECTION, SAUCES_SECTION, FILLINGS_SECTION, CONSTRUCTOR_BUTTON, PERSONAL_CABINET_BUTTON

@pytest.fixture(scope="function")
def driver():
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

class TestTransitionsPage:

    def test_transition_to_personal_cabinet(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*PERSONAL_CABINET_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_contains("account/profile"))
        assert "account/profile" in driver.current_url

    def test_transition_from_personal_cabinet_to_constructor(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(*CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_logout(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/account/profile")
        driver.find_element(*LOGOUT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    def test_transition_to_buns_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        buns_section = driver.find_element(*BUNS_SECTION)
        initial_class = buns_section.get_attribute("class")
        buns_section.click()
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(*BUNS_SECTION).get_attribute("class") != initial_class
        )
        content = driver.find_element(By.XPATH, '//div[contains(@class, "content") and contains(text(), "Булки")]')
        assert "Булки" in content.text

    def test_transition_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        sauces_section = driver.find_element(*SAUCES_SECTION)
        initial_class = sauces_section.get_attribute("class")
        sauces_section.click()
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(*SAUCES_SECTION).get_attribute("class") != initial_class
        )
        content = driver.find_element(By.XPATH, '//div[contains(@class, "content") and contains(text(), "Соусы")]')
        assert "Соусы" in content.text

    def test_transition_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        fillings_section = driver.find_element(*FILLINGS_SECTION)
        initial_class = fillings_section.get_attribute("class")
        fillings_section.click()
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(*FILLINGS_SECTION).get_attribute("class") != initial_class
        )
        content = driver.find_element(By.XPATH, '//div[contains(@class, "content") and contains(text(), "Начинки")]')
        assert "Начинки" in content.text

