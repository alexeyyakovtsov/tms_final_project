from selenium.webdriver.common.by import By


PAGE_TITLE = (By.XPATH, '//span[@class="title"]')
FIRST_NAME_FIELD = (By.XPATH, '//input[@data-test="firstName"]')
LAST_NAME_FIELD = (By.XPATH, '//input[@data-test="lastName"]')
POSTAL_CODE_FIELD = (By.XPATH, '//input[data-test="postalCode"]')
CONTINUE_BUTTON = (By.XPATH, '//input[@data-test="continue"]')
