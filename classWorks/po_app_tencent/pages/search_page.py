from time import sleep

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException

from classWorks.po_app_tencent.pages.base_page import BasePage
from classWorks.po_app_tencent.pages.personalMessage_page import PersonalMessagePage


class SearchPage(BasePage):
    def search_and_click(self, search_content):
        self.find_and_sendKeys(MobileBy.XPATH, "//*[@text='搜索']", search_content)
        sleep(1)
        elements = self.finds(MobileBy.XPATH, f"//*[@text='{search_content}']")
        if len(elements) > 1:
            elements[-1].click()
            return len(elements), PersonalMessagePage(self.driver)
        else:
            raise NoSuchElementException(f"没有找到匹配的元素：{search_content}")

    def search(self, search_content):
        elements = self.finds(MobileBy.XPATH, f"//*[@text='{search_content}']")
        return len(elements)

    def vertify_del_ok(self, real_count, except_count, search_content, msg=""):
        try:
            if real_count == except_count+1:
                print(f"{msg}'{search_content}'成功")
        except Exception as e:
            print(f"{msg}'{search_content}'失败， 原因： {e}")
        finally:
            self.back_page(MobileBy.XPATH, "//*[@text='工作台']")




