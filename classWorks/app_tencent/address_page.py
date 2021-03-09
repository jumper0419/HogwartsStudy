from random import random
from classWorks.app_tencent.base import Base


class AddressPage(Base):
    def __init__(self, driver, username="", phone=""):
        self.driver = driver
        self.username = username
        self.phone = phone

    def add_member(self):
        locat = "//*[@class='android.widget.TextView' and @text='添加成员']"
        # 最大翻5页, 默认是3页
        self.findElementAndClick(locat)
        # self.findElementAndClick(locat, 5)
        man_add = ""
        self.driver.find_element_by_id("com.tencent.wework:id/cth").click()
        self.driver.find_element_by_xpath("//*[contains(@text, '姓名')]/../*[contains(@text, '必填')]").send_keys(self.username)
        self.driver.find_element_by_xpath("//*[@class='android.widget.TextView' and contains(@text, '手机')]/..//*[contains(@text, '必填')]").send_keys(self.phone+int(random()*100))
        self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()
        # 可以看当前页面的布局，也可以看到toast控件名：//*[@class=“android.widget.Toast”]
        # print(self.driver.page_source)
        # assert '添加成功' in self.driver.page_source
        self.driver.back()
        self.driver.back()
        self.driver.find_element_by_xpath("//*[@text='消息']").click()