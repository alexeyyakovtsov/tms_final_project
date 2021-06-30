import time

import allure

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.confirm_page import ConfirmPage
from pages.overview_page import OverViewPage
from pages.complete_page import CompletePage

PAGE_TITLE = 'Products'
PRODUCT_TITLE = 'Sauce Labs'
PRODUCT_NAME = 'Sauce Labs Backpack'
CART_PAGE_TITLE = 'Your Cart'
CONFIRM_PAGE_TITLE = 'Your Information'
OVERVIEW_TITLE = 'Overview'
COMPLETE_TITLE = 'Complete!'
COMPLETE_TEXT = 'THANK YOU FOR YOUR ORDER'
ERROR_MESSAGE = 'Epic sadface: Sorry, this user has been locked out.'


@allure.story("Test 1 - get one order")
def test_case_one(driver):
    """
    Тест 1
    1. Авторизоваться на портале
    2. Добавить любой товар в корзину
    3. Перейти в корзину
    4. Подтвердить заказ
    5. Заполнить информацию заказа
    6. Завершить заказ
    7. Проверить что заказ успешно завершен
    """

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    confirm_page = ConfirmPage(driver)
    overview_page = OverViewPage(driver)
    complete_page = CompletePage(driver)

    with allure.step('Open login page'):
        driver.get('https://www.saucedemo.com/')
        assert driver.current_url == 'https://www.saucedemo.com/'
    with allure.step('Login with credentials'):
        login_page.enter_credantials('standard_user', 'secret_sauce')
        login_page.click_login_button()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        page_title = product_page.get_page_title()
        assert PAGE_TITLE.upper() in page_title
        cart_title = product_page.check_product_title(PRODUCT_NAME)
        assert PRODUCT_TITLE in cart_title
    with allure.step('Add product'):
        product_page.add_product_to_cart(1)
    with allure.step('Open cart page'):
        product_page.open_cart_page()
        cart_page_title = product_page.get_page_title()
    with allure.step('Check product in cart page'):
        assert CART_PAGE_TITLE.upper() in cart_page_title
        cart_product_name = cart_page.get_product_title()
        cart_product_price = cart_page.get_product_price()
        assert PRODUCT_NAME in cart_product_name
        assert cart_product_price in '$29.99'
    with allure.step('Go to the next step - Confirm shooping'):
        cart_page.checkout_shopping()
        confirm_title = product_page.get_page_title()
        assert CONFIRM_PAGE_TITLE.upper() in confirm_title
    with allure.step('Enter information about member'):
        confirm_page.fill_confirn_form('Test', 'Test', '123123')
        confirm_page.confirm_information_form()
        overview_page_title = product_page.get_page_title()
    with allure.step('Check global product information'):
        assert OVERVIEW_TITLE.upper() in overview_page_title
        overview_product_title = overview_page.get_product_title(PRODUCT_NAME)
        overview_product_price = overview_page.get_product_price('$29.99')
        assert PRODUCT_NAME in overview_product_title
        assert '$29.99' in overview_product_price
        overview_page.check_total_price()
        overview_page.finish_card_registration()
    with allure.step('Check overview page'):
        complete_page_title = product_page.get_page_title()
        assert COMPLETE_TITLE.upper() in complete_page_title
        complete_header = complete_page.get_complete_header()
        assert complete_header in COMPLETE_TEXT
    with allure.step('Go to home page'):
        complete_page.back_to_home()


@allure.story("Test 2 - get product with min price")
def test_case_two(driver):
    """
    Тест 2
    1. Авторизоваться на портале
    2. Отсортировать товары от минимального до максимального (по цене)
    3. Добавить товар с минимальной ценой в корзину
    4. Перейти в корзину
    5. Подтвердить заказ
    6. Заполнить информацию заказа
    7. Завершить заказ
    8. Проверить что заказ успешно завершен
    """

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    confirm_page = ConfirmPage(driver)
    overview_page = OverViewPage(driver)
    complete_page = CompletePage(driver)

    with allure.step('Open login page'):
        driver.get('https://www.saucedemo.com/')
        assert driver.current_url == 'https://www.saucedemo.com/'
    with allure.step('Login with credentials'):
        login_page.enter_credantials('standard_user', 'secret_sauce')
        login_page.click_login_button()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        page_title = product_page.get_page_title()
        assert PAGE_TITLE.upper() in page_title
        cart_title = product_page.check_product_title(PRODUCT_NAME)
        assert PRODUCT_TITLE in cart_title
    with allure.step('Add product with minimal price'):
        product_page.sort_products('Price (low to high)')
        product_page.add_product_to_cart(1)
    with allure.step('Open cart page'):
        product_page.open_cart_page()
    with allure.step('Check product in cart page'):
        cart_page_title = product_page.get_page_title()
        assert CART_PAGE_TITLE.upper() in cart_page_title
        cart_product_price = cart_page.get_product_price()
        assert cart_product_price in '$7.99'
    with allure.step('Go to the next step - Confirm shooping'):
        cart_page.checkout_shopping()
        confirm_title = product_page.get_page_title()
        assert CONFIRM_PAGE_TITLE.upper() in confirm_title
    with allure.step('Enter information about member'):
        confirm_page.fill_confirn_form('Test', 'Test', '123123')
        confirm_page.confirm_information_form()
        overview_page_title = product_page.get_page_title()
    with allure.step('Check global product information'):
        assert OVERVIEW_TITLE.upper() in overview_page_title
        overview_product_price = overview_page.get_product_price('$7.99')
        assert '$7.99' in overview_product_price
        overview_page.check_total_price()
        overview_page.finish_card_registration()
    with allure.step('Check overview page'):
        complete_page_title = product_page.get_page_title()
        assert COMPLETE_TITLE.upper() in complete_page_title
        complete_header = complete_page.get_complete_header()
        assert complete_header in COMPLETE_TEXT
    with allure.step('Go to home page'):
        complete_page.back_to_home()


@allure.story("Test 3 - delete product from cart page")
def test_case_three(driver):
    """
    Тест 3
    1. Авторизоваться на портале
    2. Отсортировать товары в обратном алфавитном порядке
    3. Добавить товар в корзину
    4. Перейти в корзину
    5. Удалить заказ
    6. Проверить что заказ удален (корзина должна быть пуста)
    7. Вернуться на страницу товаров
    """

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    with allure.step('Open login page'):
        driver.get('https://www.saucedemo.com/')
        assert driver.current_url == 'https://www.saucedemo.com/'
    with allure.step('Login with credentials'):
        login_page.enter_credantials('standard_user', 'secret_sauce')
        login_page.click_login_button()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        page_title = product_page.get_page_title()
        assert PAGE_TITLE.upper() in page_title
        cart_title = product_page.check_product_title(PRODUCT_NAME)
        assert PRODUCT_TITLE in cart_title
    with allure.step('Sort alphabetically'):
        product_page.sort_products('Name (Z to A)')
        product_page.add_product_to_cart(1)
        product_page.open_cart_page()
        cart_page_title = product_page.get_page_title()
        assert CART_PAGE_TITLE.upper() in cart_page_title
    with allure.step('Remove product'):
        cart_page.remove_product()
        assert cart_page.removed_container() is None
        cart_page.continue_shopping()


@allure.story("Test 4 - login problem user")
def test_case_four(driver):
    """
    Тест 4
    1. Авторизоваться на портале заблоченым пользователем
    2. Проверить что отображается ошибка что пользователь заблокирован
    """

    with allure.step('Open login page'):
        login_page = LoginPage(driver)
        driver.get('https://www.saucedemo.com/')
        assert driver.current_url == 'https://www.saucedemo.com/'
    with allure.step('Login problem user'):
        login_page.enter_credantials('locked_out_user', 'secret_sauce')
        login_page.click_login_button()
    with allure.step('Check error'):
        error_message = login_page.get_error_message()
        assert error_message in ERROR_MESSAGE


@allure.story("Test 5 - buy all products")
def test_case_five(driver):
    """
    Тест 5
    1. Авторизоваться на портале
    2. Добавить ВСЕ товары в корзину
    3. Перейти в корзину
    4. Подтвердить заказ
    5. Заполнить информацию заказа
    6. Завершить заказ
    7. Проверить что заказ успешно завершен
    """
    login_page = LoginPage(driver)
    product_page = ProductPage(driver)
    cart_page = CartPage(driver)
    confirm_page = ConfirmPage(driver)
    overview_page = OverViewPage(driver)
    complete_page = CompletePage(driver)

    with allure.step('Open login page'):
        driver.get('https://www.saucedemo.com/')
        assert driver.current_url == 'https://www.saucedemo.com/'
    with allure.step('Login with credentials'):
        login_page.enter_credantials('standard_user', 'secret_sauce')
        login_page.click_login_button()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        page_title = product_page.get_page_title()
        assert PAGE_TITLE.upper() in page_title
        cart_title = product_page.check_product_title(PRODUCT_NAME)
        assert PRODUCT_TITLE in cart_title
    with allure.step('Add three product into cart'):
        product_page.add_product_to_cart(1)
        product_page.add_product_to_cart(2)
        product_page.add_product_to_cart(3)
        product_page.open_cart_page()
        cart_page_title = product_page.get_page_title()
        assert CART_PAGE_TITLE.upper() in cart_page_title
        cart_page.checkout_shopping()
        confirm_title = product_page.get_page_title()
        assert CONFIRM_PAGE_TITLE.upper() in confirm_title
    with allure.step('Enter information about member'):
        confirm_page.fill_confirn_form('Test', 'Test', '123123')
        confirm_page.confirm_information_form()
        overview_page_title = product_page.get_page_title()
        assert OVERVIEW_TITLE.upper() in overview_page_title
    with allure.step('Check total price'):
        overview_page.check_total_price()
        overview_page.finish_card_registration()
    with allure.step('Check overview page'):
        complete_page_title = product_page.get_page_title()
        assert COMPLETE_TITLE.upper() in complete_page_title
        complete_header = complete_page.get_complete_header()
        assert complete_header in COMPLETE_TEXT
    with allure.step('Go to home page'):
        complete_page.back_to_home()
    

@allure.story("Test 6 - check exit from portal")
def test_case_six(driver):
    """
    Тест 6
    1. Авторизоваться на портале
    2. Открыть бургер-меню
    3. Кликнуть на кнопку Logout
    4. Проверить что пользователь перенаправлен на страницу авторизации
    """

    login_page = LoginPage(driver)
    product_page = ProductPage(driver)

    with allure.step('Open login page'):
        driver.get('https://www.saucedemo.com/')
        assert driver.current_url == 'https://www.saucedemo.com/'
    with allure.step('Login with credentials'):
        login_page.enter_credantials('standard_user', 'secret_sauce')
        login_page.click_login_button()
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
        page_title = product_page.get_page_title()
        assert PAGE_TITLE.upper() in page_title
    with allure.step('Open global menu and click logout'):
        product_page.open_menu()
        time.sleep(0.5)
        product_page.choose_menu_item('Logout')
    with allure.step('Check logout'):
        assert driver.current_url == 'https://www.saucedemo.com/'
