from appium.webdriver.common.mobileby import MobileBy

from classWorks.ui_framework.pages.app import App
from classWorks.ui_framework.pages.base_page import BasePage


class TestDecorator:

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.app.start()

    def teardown(self):
        self.app.stop()

    # 测试作业一：打开需求，点击行情
    def test_hangqing(self):
        self.app.goto_main().goto_hangqing()

    def test_a(self):
        self.base = BasePage()
        self.base.a()

    # 掉不起来，报find_decorator() missing 1 required positional argument: 'func'
    def test_find(self):
        self.base = BasePage()
        self.base.find_and_click(MobileBy.XPATH, "//*[@text='行情']")