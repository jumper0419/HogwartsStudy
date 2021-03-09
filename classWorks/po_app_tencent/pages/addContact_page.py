from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.base_page import BasePage
from classWorks.po_app_tencent.pages.editContact_page import EditContactPage


class AddContactPage(BasePage):
    def manual_add_member(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='手动输入添加']")
        return EditContactPage(self.driver)