import time

from pages.registration_page import RegistrationPage

def test_go_to_registration(browser):
    link = 'http://34.141.58.52:8080/#/register'
    page = RegistrationPage(browser, link)
    page.open()
    page.go_to_registration()
