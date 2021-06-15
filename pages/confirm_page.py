from pages.BasePage import BasePage
from locators import confirm_page_locators


class ConfirmPage(BasePage):

    def fill_confirn_form(self, firstname, lastname, postalcode):
        firstname_field = self.find_element(confirm_page_locators.FIRST_NAME_FIELD)
        lastname_field = self.find_element(confirm_page_locators.LAST_NAME_FIELD)
        postalcode_field = self.find_element(confirm_page_locators.POSTAL_CODE_FIELD)

        firstname_field.send_keys(firstname)
        lastname_field.send_keys(lastname)
        postalcode_field.send_keys(postalcode)

    def confirm_information_form(self):
        coninue_button = self.find_element(confirm_page_locators.CONTINUE_BUTTON)
        coninue_button.click()
