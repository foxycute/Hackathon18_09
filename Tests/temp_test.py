from src.Pages import BasePage
from src.Locators import YandexMainPage
import time


def test_temp(browser):
    """Тест на основе BasePage"""
    page = BasePage(browser)
    page.input(YandexMainPage.Example.yandex_input, 'Hacathon')
    page.click(YandexMainPage.Example.yandex_button)
    time.sleep(5)

