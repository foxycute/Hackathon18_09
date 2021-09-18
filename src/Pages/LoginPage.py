from .BasePage import BasePage
from src.Locators import LoginPage
from src.Services.Faker.FakeDataGenerator import DataGenerator


class Login(BasePage):
    def create_account(self):
        data = DataGenerator()
        self.select(LoginPage.CreateCustomer.title, 'Mr.')
        self.input(LoginPage.CreateCustomer.first_name, data.get_name())
        self.input(LoginPage.CreateCustomer.last_name, data.get_name())
        self.input(LoginPage.CreateCustomer.email, data.get_email())
        self.input(LoginPage.CreateCustomer.password, 'evetah799')
        self.input(LoginPage.CreateCustomer.confirm_password, 'evetah799')
        self.click(LoginPage.CreateCustomer.consent_checkbox)
        self.click(LoginPage.CreateCustomer.terms_checkbox)
        self.click(LoginPage.CreateCustomer.register_button)


