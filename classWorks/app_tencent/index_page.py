from appium.webdriver.common.mobileby import MobileBy

from classWorks.app_tencent.address_page import AddressPage
from classWorks.app_tencent.base import Base


class IndexPage(Base):
    def __init__(self, username="", phone=""):
        self.setup()
        self.username = username
        self.phone = phone

    def goto_address(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.TextView' and @text='通讯录']").click()
        return AddressPage(self.driver, self.username, self.phone)