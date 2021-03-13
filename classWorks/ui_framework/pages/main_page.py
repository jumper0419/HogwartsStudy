from appium.webdriver.common.mobileby import MobileBy

from classWorks.ui_framework.pages.base_page import BasePage


class MainPage(BasePage):

    def goto_hangqing(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='行情']")
