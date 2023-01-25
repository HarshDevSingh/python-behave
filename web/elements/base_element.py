import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException


class BaseElement(object):
    def __init__(self, locator, selector, context):
        self.locator = locator
        self.selector = selector
        self.context = context

    def is_element_clickable(self) -> bool:
        try:
            element = WebDriverWait(self.context.browser, 10).until(
                EC.element_to_be_clickable((self.locator, self.selector)))
            return element
        except ElementNotInteractableException as e:
            print(e)
            return False

    def _find_element(self):
        return self.context.browser.find_element(self.locator, self.selector)

    def is_element_visible(self):
        element = self._find_element()
        if element.is_displayed():
            return True
        else:
            return False

    def send_keys(self,keys):
        element = self._find_element()
        if element:
            element.send_keys(keys)
        else:
            raise Exception(f"Failed to send keys to element {self.selector}")

    def click(self):
        element = self._find_element()
        if element:
            element.click()
        else:
            raise Exception(f"Failed to click {self.selector}")




