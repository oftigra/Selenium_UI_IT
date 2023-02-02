import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('3@ya.ru')
        login_pass = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_pass.send_keys('22222')
        login_btn = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_btn.submit()
        time.sleep(5)



