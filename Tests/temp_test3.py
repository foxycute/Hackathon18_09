from src.Pages.LoginPage import Login
import time


def test_yandex_page(browser):
    """Тест на основе YandexPage"""
    page = Login(browser)
    page.create_account()
    time.sleep(5)

