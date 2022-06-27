import time
from .pages.product_page import ProductPage

# Переходим на страницу с товаром
def test_guest_add_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_button_add_book()
    page.solve_quiz_and_get_code()
    page.checking_book_added_to_cart_price()
    page.checking_book_added_to_cart_name()




