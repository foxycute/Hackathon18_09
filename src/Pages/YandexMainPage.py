from .BasePage import BasePage
from src.Locators import YandexMainPage


class YandexPage(BasePage):
    def search_hacathon(self):
        self.input(YandexMainPage.Example.yandex_input, 'Hacathon')
        self.click(YandexMainPage.Example.yandex_button)

