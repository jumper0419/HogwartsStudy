from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.base_page import BasePage


class PersonalMessageDetailPage(BasePage):
    def edit_name(self):
        pass

    def del_contact(self):
        self.swip_find(MobileBy.XPATH, "//*[@text='删除成员']").click()
        self.find_and_click(MobileBy.XPATH, "//*[@text='确定']")
