import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


black_list = yaml.safe_load(open("../datas/black.yml", encoding='utf-8'))


def b(func):
    def run(*args, **kwargs):
        print("hello")
        func(*args, **kwargs)

    return run


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    def find_decorator(self, func):
        def run(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                for exe_xpath in black_list:
                    element = self.driver.find_elements(MobileBy.XPATH, exe_xpath)
                    if len(element) >= 1:
                        element[0].click()
                        self.find_decorator(func)
        return run

    @find_decorator
    def find(self, locator, value):
        self.driver.find_element(locator, value)

    def finds(self, locator, value):
        self.driver.find_elements(locator, value)

    @find_decorator
    def find_and_click(self, locator, value):
        self.driver.find_element(locator, value).click()

    def find_and_sendKeys(self, locator, value, text):
        self.driver.find_element(locator, value).send_keys(text)

    @b
    def a(self):
        print("JSON")