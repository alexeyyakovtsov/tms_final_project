import BasePage

from locators import login_page_locators


class LoginPage(BasePage):
    
    def enter_valid_credantials(self, element):
        valid_username = self.login_page_locators(element)
        valid_password = self.find_element(login_page_locators.PASSWORD_CREDENTIALS)

        user_name_field = self.find_element(login_page_locators.USERNAME_FIELD)
        password_field = self.find_element(login_page_locators.PASSWORD_FIELD)
        
        user_name_field.send_keys(valid_username)
        password_field.send_keys(valid_password)

    
    def click_login_button(self):
        login_btn = self.find_element(login_page_locators.LOGIN_BUTTON)
        login_btn.click()
