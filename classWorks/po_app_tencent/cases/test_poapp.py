from time import sleep

import pytest
import yaml
from appium.webdriver.common.mobileby import MobileBy

from classWorks.po_app_tencent.pages.app import App

datas = yaml.safe_load(open('../datas/members.yml', encoding='utf-8'))
class TestPoApp():
    def setup_class(self):
        self.app = App()

    def setup(self):
        self.app.start()

    def teardown(self):
        self.app.stop()

    @pytest.mark.parametrize('name, phone, button_text, vertify_func, vertify_text', datas)
    def test_add_member(self, name, phone, button_text, vertify_func, vertify_text):
        try:
            element = self.app.goto_main().goto_addressList().add_contact().manual_add_member()
            element.fast_input(name, phone, button_text)
            element.vertify_save_ok(vertify_func, vertify_text)
        finally:
            # 保证后续的数据能够正常运行
            self.app.goto_main().back_page(MobileBy.XPATH, "//*[@text='工作台']")


    def test_del_member(self):
        try:
            search_count = "赵三"
            func_name = "删除成员"
            search_page = self.app.goto_main().goto_addressList().goto_search()
            element_len, personMesPage = search_page.search_and_click(search_count)
            personMesPage.click_more().edit_person().del_contact()
            real_count = search_page.search(search_count)
            search_page.vertify_del_ok(real_count, element_len, search_count, func_name)
        finally:
            # 保证后续的数据能够正常运行
            self.app.goto_main().back_page(MobileBy.XPATH, "//*[@text='工作台']")
