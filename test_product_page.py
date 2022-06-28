from .pages.product_page import ProductPage
import pytest

bugged_link = ['7']

# Перечисляем номера. Маркируем пропуск плохого теста.
@pytest.mark.parametrize('number_url', ['0', '1', '2', '3', '4', '5', '6',
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  '8', '9'])
# Переходим на страницу с товаром
def test_guest_add_to_basket(browser, number_url):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{str(number_url)}'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_button_add_book()
    page.solve_quiz_and_get_code()
    page.checking_button_checkout() # Проверка появления кнопки Оформить
    page.checking_book_added_to_cart_price() # Проверка соответствия цены на складе и в корзине
    page.checking_book_added_to_cart_name() # Проверка соответствия имени товара на складе и в корзине
    page.output_current_link()





