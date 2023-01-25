from behave import *
from web.page_objects.swag_labs.login_page import LoginPage
from utilities.test_data.test_data import TestData


@given(u'I open saucedemo.com')
def open_saucedemo(context):
    login = LoginPage(context)
    login.open()


@then(u'I login as "{username}"')
def login_into_saucedemo(context, username : str):
    login = LoginPage(context)
    login.enter_username(username)
    login.enter_password(TestData.USER_LOGIN_DATA.get(username))
    login.submit_login_form()
