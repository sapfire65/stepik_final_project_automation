from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.XPATH, '//a[@id="login_link"]')
    BASKET_BUTTON = (By.XPATH, '//a[@class="btn btn-default"]')

class BasketPageLocators():
    BASKET_ORDERING = (By.XPATH, '//img[@class="thumbnail"]')
    BASKET_TEXT_BASKET_IS_EMPTY = (By.XPATH, '//div[@id="content_inner"]')

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
    PRICE_IN_THE_CART = '(//strong)[6]'
    STOCK_PRICE_BOOK = '//p[@class="price_color"]'
    NAME_IN_THE_CART = '(//div[@class="alertinner "]/strong)[1]'
    STOCK_NAME_BOOK = '//h1'
    SUCCESS_MESSAGE = (By.XPATH, '(//div[@class="alertinner "])[1]')




