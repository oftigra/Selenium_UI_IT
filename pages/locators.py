from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#app > header > div > ul > li:nth-child(1) > a > span")


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.CSS_SELECTOR, "#password > input")
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")

class RegistrationPageLocators:
    REGISTRATION_EMAIL = (By.ID, "login")
    REGISTRATION_PASS = (By.XPATH, "//*[@id='password']/input")
    REGISTRATION_CONFIRM_PASS = (By.CSS_SELECTOR, "#confirm_password > input")
    REGISTRATION_SUBMIT_BTN = (By.CLASS_NAME, "p-button-label")
