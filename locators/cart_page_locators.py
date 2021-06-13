from selenium.webdriver.common.by import By


PAGE_TITLE = (By.XPATH, '//span[@class="title"]')
CARD_ITEM_BLOCK = (By.XPATH, '//div[@class="cart_item"]')
CARD_ITEM_NAME = (By.XPATH, '//div[@class="inventory_item_name"]')
REMOVE_CARD_BUTTON = (By.XPATH, '//button[contains(.,"Remove")]')
CHECKOUT_BUTTON = (By.XPATH, '//button[@data-test="checkout"]')
CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//button[@data-test="continue-shopping"]')
