from web.elements.element_factory import ElementFactory
from selenium.webdriver.common.by import By
from .base_swaglabs_page import BaseSwagLabsPage


class LoginPage(BaseSwagLabsPage):
    def __init__(self,context):
        super().__int__(context)
        self.username_field = ElementFactory(By.XPATH,"//*[@id=\"user-name\"]", context)
        self.password_field = ElementFactory(By.XPATH, "//*[@id=\"password\"]", context)
        self.login_btn = ElementFactory(By.XPATH,"//*[@id=\"login-button\"]",context)

    def enter_username(self,keys):
        if self.username_field.element().is_element_visible():
            self.username_field.element().send_keys(keys)
        else:
            raise Exception("failed to enter email")

    def enter_password(self,keys):
        if self.password_field.element().is_element_visible():
            self.password_field.element().send_keys(keys)
        else:
            raise Exception("failed to enter password")

    def submit_login_form(self):
        if self.login_btn.element().is_element_visible() and self.login_btn.element().is_element_clickable():
            self.login_btn.element().click()
        else:
            raise Exception("failed to submit login form")


