from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __element(self, selectors: dict):
        for search_type in selectors.keys():
            try:
                return self.driver.find_element(getattr(By, search_type), selectors[search_type])
            except NoSuchElementException:
                print('\nERROR: SELECTOR ' + selectors[search_type] + ' IN ' + search_type + ' IS FALSE')
                continue
            except AttributeError:
                print('\nERROR: ATTRIBUTE ERROR OF BY.')
                continue
        raise NoSuchElementException

    def click(self, selector):
        ActionChains(self.driver).move_to_element(self.__element(selector)).click().perform()

    def input(self, selector, value):
        element = self.__element(selector)
        element.clear()
        element.send_keys(value)

    def select(self, selector, value):
        Select(self.__element(selector)).select_by_visible_text(value)
