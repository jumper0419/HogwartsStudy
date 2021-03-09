from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.base_page import BasePage
from classWorks.po_app_tencent.pages.editPersonalMessage_page import EditPersonalMessagePage


class PersonalMessagePage(BasePage):
    def click_more(self):
        self.find_and_click(MobileBy.XPATH, "//*[@text='个人信息']/../../../../..//*[@class='android.widget.RelativeLayout']")
        return EditPersonalMessagePage(self.driver)