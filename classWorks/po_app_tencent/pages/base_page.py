from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def find_and_click(self, locator, value):
        return self.driver.find_element(locator, value).click()

    def find_and_sendKeys(self, locator, value, text):
        return self.driver.find_element(locator, value).send_keys(text)

    def swip(self):
        size = self.driver.get_window_size()
        width = size.get('width')
        height = size.get('height')
        self.driver.swipe(width*1/2, height*4/5, width*1/2, height*1/5)

    def swip_find(self, locator, value, num=3):
        for i in range(num):
            if i == num - 1:
                self.driver.implicitly_wait(5)
                raise NoSuchElementException(f"翻页{num}次，没有找到这样的元素")

            self.driver.implicitly_wait(1)
            try:
                element = self.driver.find_element(locator, value)
                return element
            except:
                # print("翻屏中...")
                self.swip()

    def swip_finds(self, locator, value):
        # while True:
            pass

    def back_page(self, locator, value):
        while True:
            try:
                self.driver.find_element(locator, value)
                break
            except:
                self.driver.back()




