from faker import Faker
from faker.providers.phone_number import ru_RU


class DataGenerator:
    """
    Use 'locale' to change data for any countries
    """

    def __init__(self, locale='en_US'):
        self.faker = Faker(locale=locale)

    def get_name(self):
        return self.faker.name()

    def get_email(self):
        return self.faker.free_email()

    def get_company_name(self):
        return self.faker.company()

