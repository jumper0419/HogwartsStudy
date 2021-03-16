from selenium import webdriver


class TestSwip:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.baidu.com")

    def test_swip(self):
        windows = self.driver.get_window_size()
        print(windows)
        width = windows["width"]
        height = windows["height"]
        print(width)