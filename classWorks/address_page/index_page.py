from selenium import webdriver

from classWorks.address_page.address_page import AddressPage


class IndexPage:
    def __init__(self, username="", phone="", acctid=""):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9432'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.username = username
        self.phone = phone
        self.acctid = acctid

    def goto_address(self):
        self.driver.find_element_by_css_selector('#menu_contacts').click()
        return AddressPage(self.driver, username=self.username, phone=self.phone, acctid=self.acctid)