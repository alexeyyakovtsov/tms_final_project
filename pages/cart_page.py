from pages.BasePage import BasePage
from locators import cart_page_locators


class CartPage(BasePage):

    def get_product_title(self):
        return self.get_element_title(cart_page_locators.CARD_ITEM_NAME)

    def get_product_price(self):
        return self.get_element_title(cart_page_locators.ITEM_PRICE)

    def remove_product(self):
        remove_button = self.find_element(cart_page_locators.REMOVE_CARD_BUTTON)
        remove_button.click()

    def continue_shopping(self):
        continue_shopping_button = self.find_element(cart_page_locators.CONTINUE_SHOPPING_BUTTON)
        continue_shopping_button.click()
    
    def checkout_shopping(self):
        checkout_button = self.find_element(cart_page_locators.CHECKOUT_BUTTON)
        self.move_to_element(checkout_button)
        checkout_button.click()

    def removed_container(self):
        return self.check_absence_element(cart_page_locators.REMOVED_ITEMS)
