from selenium import webdriver

from webAuto.address_page.address_page import AddressPage


class MainPage:
    def __init__(self, username="", phone="", acctid=""):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = '127.0.0.1:9432'
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.username = username
        self.phone = phone
        self.acctid = acctid

    def goto_address(self):
        self.driver.find_element_by_css_selector('#menu_contacts').click()
        return AddressPage(self.driver, username=self.username, phone=self.phone, acctid=self.acctid)