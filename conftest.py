import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help="Choose browser")
    parser.addoption(
        '--url',
        action='store',
        default="https://yandex.ru",
        help="Choose url")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver
