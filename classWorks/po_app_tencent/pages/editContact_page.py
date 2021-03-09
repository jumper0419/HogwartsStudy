from random import random

from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.base_page import BasePage


class EditContactPage(BasePage):
    # 姓名和电话添加，点击保存
    def fast_input(self, name, phone, text):
        self.find_and_sendKeys(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']", name)
        self.find_and_sendKeys(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='必填']", phone+int(random()*100))
        self.find_and_click(MobileBy.XPATH, f"//*[@text='{text}']")

    def vertify_save_ok(self, text, message=""):
        try:
            self.find(MobileBy.XPATH, f"//*[@text='{text}']")
            print(f"{message} 成功")
        except Exception as e:
            print(f"{message} 失败，原因：{e}")
        finally:
            self.back_page(MobileBy.XPATH, "//*[@text='工作台']")

    #  todo
    def all_input(self, name, phone, text, acttid=''):
        pass