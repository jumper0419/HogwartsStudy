from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.addContact_page import AddContactPage
from classWorks.po_app_tencent.pages.base_page import BasePage
from classWorks.po_app_tencent.pages.search_page import SearchPage


class AddressListPage(BasePage):
    def add_contact(self):
        self.swip_find(MobileBy.XPATH, "//*[@text='添加成员']", num=5).click()
        return AddContactPage(self.driver)

    def goto_search(self):
        self.find_and_click(MobileBy.ID, "com.tencent.wework:id/igk")
        return SearchPage(self.driver)