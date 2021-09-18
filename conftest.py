import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help="Choose browser")
    parser.addoption(
        '--url',
        action='store',
        default="https://apparel-uk.local:9002/ucstorefront/en/login",
        help="Choose url")


@pytest.fixture
def browser(request):
    """ Фикстура инициализации браузера """
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise Exception(f"{request.param} is not supported!")
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.open = open
    driver.open()
    return driver
