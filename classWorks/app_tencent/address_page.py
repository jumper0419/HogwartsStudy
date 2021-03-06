from random import random
from classWorks.app_tencent.base import Base


class AddressPage(Base):
    def __init__(self, driver, username="", phone=""):
        self.driver = driver
        self.username = username
        self.phone = phone

    def add_member(self):
        locat = "//*[@class='android.widget.TextView' and @text='添加成员']"
        self.findElementAndClick(locat)
        man_add = ""
        self.driver.find_element_by_id("com.tencent.wework:id/cth").click()
        self.driver.find_element_by_id("com.tencent.wework:id/b7m").send_keys(self.username)
        self.driver.find_element_by_id("com.tencent.wework:id/fwi").send_keys(self.phone+int(random()*100))
        self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()
        self.driver.back()
        self.driver.back()