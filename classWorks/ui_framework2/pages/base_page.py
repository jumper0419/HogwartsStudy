import logging

import yaml
from appium.webdriver.webdriver import WebDriver

from classWorks.ui_framework2.pages.decorator import handle_blacklist
from classWorks.ui_framework2.pages.logger import log_init


class BasePage:
    def __init__(self, driver:WebDriver=None):
        self.driver = driver

    @handle_blacklist
    def find(self, locator, value):
        return self.driver.find_element(locator, value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    @handle_blacklist
    def find_and_click(self, locator, value):
        self.driver.find_element(locator, value).click()

    def find_and_send(self, locator, value, text):
        self.driver.find_element(locator, value).send_keys(text)

    def get_datas(self, file_path, data_name=""):
        datas = []
        if file_path != "":
            with open(file_path, encoding='utf-8') as f:
                datas = yaml.safe_load(f)
            if data_name == "":
                return datas
            else:
                return datas[data_name]
        return datas

    # 解析关键字
    def parse_keywords(self, file_path, keywords, ):
        steps = self.get_datas(file_path, keywords)
        for step in steps:
            if step['action'] == "find":
                self.find(step['locator'], step['value'])
            elif step['action'] == "finds":
                self.finds(step['locator'], step['value'])
            elif step['action'] == "find_and_click":
                self.find_and_click(step['locator'], step['value'])
            elif step['action'] == "find_and_send":
                self.find_and_send(step['locator'], step['value'], step['content'])

    # 截图
    def screenshot(self):
        return self.driver.get_screenshot_as_png()

    def log(self, log_id, log_name):
        return log_init(log_id, log_name)

