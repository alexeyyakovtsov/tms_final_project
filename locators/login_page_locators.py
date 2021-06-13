from selenium.webdriver.common.by import By


USERNAME_FIELD = (By.XPATH, '//input[@data-test="username"]')
PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')
PASSWORD_CREDENTIALS = (By.XPATH, '//div[@class="login_password"]/text()')


def get_login_credentials(elem):
    return (By.XPATH, '//div[@class="login_credentials"]/text()[{elem}]')
