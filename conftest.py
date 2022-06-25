import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# получает значения из консоли для --browser_name= и --language=
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: 'ru' or 'en'")

@pytest.fixture(scope="function")
def browser(request):
    # переменные user_language и browser_name передаются из консоли
    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = ''
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
        # Для Chrome браузера
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(10) # Не явное ожидание элементов 10 сек.
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # Чтобы указать язык браузера, использую класс Options и метод add_experimental_option
        # Для Firefox  браузера
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


