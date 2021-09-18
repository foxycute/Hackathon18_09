from behave import *
from src.Pages.LoginPage import Login
from src.Locators.LoginPage import LoginPage


@given("I have account")
def step_impl(context):
    context.user_email = 'team38@gmail.com'
    context.user_password = 'Team38'
    context.page = Login()


@when("I open Login page")
def step_impl(context):
    context.page.to_page('https://apparel-uk.local:9002/ucstorefront/en/login')


@step("enter my email and password")
def step_impl(context):
    context.page.input(LoginPage.Login.email, context.user_email)
    context.page.input(LoginPage.Login.password, context.user_password)


@step('press a button "Log in"')
def step_impl(context):
    context.page.click(LoginPage.Login.login_button)


@then("I see main page")
def step_impl(context):
    assert context.page.driver.current_url == "https://apparel-uk.local:9002/ucstorefront/en/"
