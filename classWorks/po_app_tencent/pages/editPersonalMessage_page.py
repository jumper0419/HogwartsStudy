from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.base_page import BasePage
from classWorks.po_app_tencent.pages.personalMessageDetail_page import PersonalMessageDetailPage


class EditPersonalMessagePage(BasePage):
    def edit_person(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='编辑成员']")
        return PersonalMessageDetailPage(self.driver)