import os
from classWorks.ui_framework2.pages.app import App


class TestDecorator:

    def setup_class(self):
        self.app = App()

    def setup(self):
        self.app.start()

    def teardown(self):
        self.app.stop()

    # 测试作业二：提取关键字
    def test_hangqing(self):
        self.app.goto_main().goto_market().goto_search().search()

    # def test_os(self):
    #     # G:\HogwartsStudy\classWorks\ui_framework2
    #     print(os.path.dirname(os.getcwd()))
