import time

from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_password_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        # находим и кликаем по ссылке логина
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        # time.sleep(5)
        current_url_login = self.browser.current_url
        print(current_url_login)
        assert "/login" in current_url_login, "login is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        input_login = self.browser.find_element(*LoginPageLocators.INPUT_LOGIN)
        input_login_correct = input_login.get_attribute('name')
        print(f'attribut | name = {input_login_correct}')
        assert  'login-username' in input_login_correct, 'input login not found'



    def should_be_password_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        input_password = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password_correct = input_password.get_attribute('name')
        print(f'attribut | name = {input_password_correct}')
        assert 'login-password' in input_password_correct, 'input password not found'

    def should_be_register_form(self):
        # Проверка наличия формы регистрации
        self.browser.find_element(*LoginPageLocators.LOGIN_LINK).click()
        reg_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        register_form = reg_form.get_attribute('id')
        print(f'attribut | id = {register_form}')
        assert 'register_form' in register_form, 'register form not found'

