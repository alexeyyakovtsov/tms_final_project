from pages.BasePage import BasePage
from locators import product_page_locators


class ProductPage(BasePage):

    def get_page_title(self):
        return self.get_element_title(product_page_locators.PAGE_TITLE)


    def sort_products(self, sort_value):
        sort_select = self.find_element(product_page_locators.SORT_CONAINER)
        sort_select.click()
        select_locator = product_page_locators.sort_options(sort_value)
        select_element = self.find_element(select_locator)
        select_element.click()


    def add_product_to_cart(self, elem):
        locator = product_page_locators.add_to_card_button(elem)
        element = self.find_element(locator)
        self.move_to_element(element)
        element.click()


    def open_cart_page(self):
        cart_element = self.find_element(product_page_locators.SHOPING_CART_ICON)
        cart_element.click()


    def check_product_title(self, product_title):
        return self.get_element_title(product_page_locators.get_product_title(product_title))

    
    def open_menu(self):
        burger_menu = self.find_element(product_page_locators.BURGER_MENU)
        burger_menu.click()

    
    def choose_menu_item(self, menu_name):
        menu_locator = product_page_locators.get_item_menu(menu_name)
        menu_element = self.find_element(menu_locator)
        menu_element.click()
    