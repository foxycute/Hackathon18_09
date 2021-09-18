from behave import *
from src.Pages.LoginPage import Login



@given("I open Login page")
def step_impl(context):
    context.page = Login()
    context.page.to_page('https://apparel-uk.local:9002/ucstorefront/en/login')


@when("created new user")
def step_impl(context):
    context.page.create_account()


@then("I see welcome text")
def step_impl(context):
    text = context.page.driver.find_element_by_css_selector('.alert.alert-info.alert-dismissable.getAccAlert').is_displayed()
    assert text


@step("I see main banner")
def step_impl(context):
    banner = context.page.driver.find_element_by_css_selector("img[title='Start Your Season']").is_displayed()
    assert banner
