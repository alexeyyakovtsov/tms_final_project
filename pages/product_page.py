from pages.BasePage import BasePage
from locators import product_page_locators


class ProductPage(BasePage):

    def get_page_title(self):
        return self.get_element_title(product_page_locators.PAGE_TITLE)

    def sort_products(self, sort_value):
        sort_select = self.find_element(product_page_locators.PRODUCT_SORT_CONAINER)
        sort_select.click()
        select_opt = self.product_page_locators.sort_options(sort_value)
        select_opt.click()

    def add_product_to_cart(self, product_element):
        product = self.product_page_locators.add_to_card_button(product_element)
        product.click()

    def open_cart_page(self):
        cart_element = self.find_element(product_page_locators.SHOPING_CART_ICON)
        cart_element.click()

    def check_product_title(self, product_title):
        return self.get_element_title(product_page_locators.get_product_title(product_title))
