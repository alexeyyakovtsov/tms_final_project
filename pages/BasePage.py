import typing

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def find_element(self, locator: typing.Tuple, time: int = 10) -> WebElement:
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")


    def find_elements(self, locator: typing.Tuple, time: int = 10) -> typing.List:
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")


    def move_to_element(self, web_elem: WebElement):
        ActionChains(self.driver).move_to_element(web_elem).perform()


    def check_absence_element(self, locator, time=5):
        WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))


    def get_element_title(self, locator, time=5):
        title = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator")
        return title.text


    def click_element_by_index(self, index: int, web_elem_list: typing.List):
        assert len(web_elem_list) > 0, 'No find element'
        web_elem_list[index].click()


    def get_all_elements_in_list(self, locator) -> typing.List:
        elements = self.find_elements(locator)
        assert len(elements) > 0, 'Elements not found'
        return elements


    def move_to_element_with_js(self, web_element: WebElement, locator: typing.Tuple) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
