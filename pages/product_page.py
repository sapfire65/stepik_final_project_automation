from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
import time
import math

class ProductPage(BasePage):
    # Добавить в карзину книгу
    def go_to_button_add_book(self):
        button_add_book = self.browser.find_element(*ProductPageLocators.ADD_BOOK_BUTTON)
        button_add_book.click()

    def solve_quiz_and_get_code(self):
        time.sleep(1)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

        # time.sleep(5000)

    def checking_book_added_to_cart_price(self):
        price_in_the_cart = self.browser.find_element(By.XPATH, '(//div/p/strong)[2]').text
        stock_price_book = self.browser.find_element(By.XPATH, '//p[@class="price_color"]').text
        print(f'Price book, stock / added: - {stock_price_book} / {price_in_the_cart}')
        assert price_in_the_cart == stock_price_book, 'The PRICE of the book in stock is different from the price in the cart'

    def checking_book_added_to_cart_name(self):
        name_in_the_cart = self.browser.find_element(By.XPATH, '(//div[@class="alertinner "]/strong)[1]').text
        stock_name_book = self.browser.find_element(By.XPATH, '//h1').text
        print(f'Name book, stock / added: - {stock_name_book} / {name_in_the_cart}')
        assert stock_name_book == name_in_the_cart, 'The NAME of the book in stock is different from the price in the cart'
