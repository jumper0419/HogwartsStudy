from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from classWorks.ui_framework.pages.base_page import BasePage


class MainPage(BasePage):

    def goto_hangqing(self):
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/post_status"]')
        self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")
        self.find_and_click(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/action_search"]')
        self.find_and_send(MobileBy.XPATH, '//*[@resource-id="com.xueqiu.android:id/search_input_text"]', "alibaba")
