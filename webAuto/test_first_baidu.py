from time import sleep

from selenium import webdriver


class TestBaidu:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        # self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("我是中国共产党")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='su']").click()