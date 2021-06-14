from pages.BasePage import BasePage
from locators import login_page_locators


class LoginPage(BasePage):

    def enter_credantials(self, login, password):
        user_name_field = self.find_element(login_page_locators.USERNAME_FIELD)
        password_field = self.find_element(login_page_locators.PASSWORD_FIELD)

        user_name_field.send_keys(login)
        password_field.send_keys(password)

    def click_login_button(self):
        login_btn = self.find_element(login_page_locators.LOGIN_BUTTON)
        login_btn.click()
