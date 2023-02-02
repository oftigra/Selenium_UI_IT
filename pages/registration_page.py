import time

from .base_page import BasePage
from .locators import RegistrationPageLocators


class RegistrationPage(BasePage):
    def go_to_registration(self):
        reg_email = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys("4@ya.ru")
        time.sleep(2)
        reg_pass = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_PASS)
        reg_pass.send_keys("22222")
        time.sleep(2)
        reg_confirm_pass = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_CONFIRM_PASS)
        reg_confirm_pass.send_keys("22222")
        time.sleep(2)
        reg_submit_btn = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_SUBMIT_BTN)
        reg_submit_btn.submit()
        time.sleep(1)



