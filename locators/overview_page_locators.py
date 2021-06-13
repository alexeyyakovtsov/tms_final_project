from selenium.webdriver.common.by import By


PAGE_TITLE = (By.XPATH, '//span[@class="title"]')
SUBTOTAL_PRICE_LABEL = (By.XPATH, '//div[@class="summary_subtotal_label"]')
TAX_PRICE_LABEL = (By.XPATH, '//div[@class="summary_tax_label"]')
TOTAL_PRICE_LABEL = (By.XPATH, '//div[@class="summary_total_label"]')
FINISH_BUTTON = (By.XPATH, '//button[@data-test="finish"]')



def get_product_title(name):
    return (By.XPATH, '//div[@class="inventory_item_name"][contains(.,"{name}")]')


def get_price(price):
    return (By.XPATH, '//div[@class="inventory_item_price"][contains(.,"{price}")]')