from appium.webdriver.webdriver import WebDriver

from classWorks.ui_framework.pages.decorator import b, find_decorator


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

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