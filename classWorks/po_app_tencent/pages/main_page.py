from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.addressList_page import AddressListPage
from classWorks.po_app_tencent.pages.base_page import BasePage


class MainPage(BasePage):
    def goto_addressList(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='通讯录']")
        return AddressListPage(self.driver)