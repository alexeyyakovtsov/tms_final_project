from pages.BasePage import BasePage
from locators import complete_page_locators


class CompletePage(BasePage):

    def get_complete_header(self):
        return self.get_element_title(complete_page_locators.COMPLETE_HEADER)

    def back_to_home(self):
        back_to_home_button = self.find_element(complete_page_locators.BACK_TO_PRODUCTS_BUTTON)
        back_to_home_button.click()
