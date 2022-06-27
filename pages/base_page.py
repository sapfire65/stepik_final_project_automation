import math
from selenium import webdriver
from selenium.webdriver import Remote as RemoteWebDriver

class BasePage():
    # Создаем конструкцию взаимодействия передачи ссылки в браузер
    def __init__(self, browser: RemoteWebDriver, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # Создаем метод открытия и перехода по ссылке page.open()
    def open(self):
        self.browser.get(self.url)






