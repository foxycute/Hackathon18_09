from src.Pages.YandexMainPage import YandexPage
import time


def test_yandex_page(browser):
    """Тест на основе YandexPage"""
    page = YandexPage(browser)
    page.search_hacathon()
    time.sleep(5)

