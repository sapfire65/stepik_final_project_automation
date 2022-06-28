from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    INPUT_LOGIN = (By.XPATH, '//input[@name="login-username"]')
    INPUT_PASSWORD = (By.XPATH, '//input[@name="login-password"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')

class ProductPageLocators():
    ADD_BOOK_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    CHECK_BUTTON_CLICKABILITY = '(//a[@class="btn btn-info"])[1]'




