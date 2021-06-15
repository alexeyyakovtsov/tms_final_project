from pages.BasePage import BasePage
from locators import overview_page_locators


class OverViewPage(BasePage):

    def get_product_price(self, price):
        product_price = overview_page_locators.get_price(price)
        return self.get_element_title(product_price)

    def get_product_title(self, title):
        product_title = overview_page_locators.get_product_title(title)
        return self.get_element_title(product_title)

    def get_subtotal_price(self):
        return self.get_element_title(overview_page_locators.SUBTOTAL_PRICE_LABEL)

    def get_tax_price(self):
        return self.get_element_title(overview_page_locators.TAX_PRICE_LABEL)

    def get_total_price(self):
        return self.get_element_title(overview_page_locators.TOTAL_PRICE_LABEL)

    def finish_card_registration(self):
        finish_button = self.find_element(overview_page_locators.FINISH_BUTTON)
        finish_button.click()
