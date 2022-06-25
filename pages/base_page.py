import time
from selenium import webdriver
from selenium.webdriver import Remote as RemoteWebDriver

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


