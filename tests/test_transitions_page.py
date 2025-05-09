from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGOUT_BUTTON, BUNS_SECTION, SAUCES_SECTION, FILLINGS_SECTION, CONSTRUCTOR_BUTTON, PERSONAL_CABINET_BUTTON, BUNS_CONTENT, SAUCES_CONTENT, FILLINGS_CONTENT

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
        driver.find_element(*BUNS_SECTION).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(BUNS_CONTENT))
        content = driver.find_element(*BUNS_CONTENT)
        assert "Булки" in content.text

    def test_transition_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*SAUCES_SECTION).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(SAUCES_CONTENT))
        content = driver.find_element(*SAUCES_CONTENT)
        assert "Соусы" in content.text

    def test_transition_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*FILLINGS_SECTION).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(FILLINGS_CONTENT))
        content = driver.find_element(*FILLINGS_CONTENT)
        assert "Начинки" in content.text
