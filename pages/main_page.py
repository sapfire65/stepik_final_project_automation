from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from selenium.webdriver.common.by import By
import time


class MainPage(BasePage):
    pass



    # # Проверяем наличие ссылки на страницу логина.
    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    #
    # # Если элемент найден возвращаем True, иначе перехватываем ошибку 'NoSuchElementException' и присваиваем False
    # def is_element_present(self, how, what):
    #     try:
    #         self.browser.find_element(how, what)
    #     except (NoSuchElementException):
    #         return False
    #     return True








