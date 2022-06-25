# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# # from selenium.webdriver.chrome.options import Options
#
#
# link = "http://selenium1py.pythonanywhere.com/"
# link_2 = '/catalogue/coders-at-work_207/'
#
# def test_button_add_product(browser):
#     browser.get(f'{link}{link_2}')
#     # time.sleep(30)
#     # Явное ожидание кнопки добавления
#     button = WebDriverWait(browser, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')))
#
#     # Проверка наличия кнопки по значению атрибута 'type'
#     check_atribut = button.get_attribute('type')
#     assert str(check_atribut) == 'submit', '\nКнопка добавления, не обнаружена'


from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина











