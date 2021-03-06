from selenium.webdriver.common.by import By


BURGER_MENU = (By.XPATH, '//div[@class="bm-burger-button"]')
SORT_CONAINER = (By.XPATH, '//select[@data-test="product_sort_container"]')
SHOPING_CART_ICON = (By.XPATH, '//div[@class="shopping_cart_container"]')
PAGE_TITLE = (By.XPATH, '//span[@class="title"]')
REMOVE_BUTTON = (By.XPATH, '//button[contains(.,"Remove")]')


def get_product_title(name):
    return (By.XPATH, f'//div[@class="inventory_item_name"][contains(.,"{name}")]')


def add_to_card_button(elem):
    return (By.XPATH, f'(//button[contains(.,"Add to cart")])[{elem}]')


def sort_options(sort_value):
    return (By.XPATH, f'//option[contains(., "{sort_value}")]')


def get_item_menu(name):
    return (By.XPATH, f'//a[@class="bm-item menu-item"][contains(.,"{name}")]')
