"""
用debug模式调试：只会在一个窗口进行所有的测试用例
即：如果你的测试用例有2个，先打开百度，然后再去打开好搜，是同一个窗口进行
"""


from time import sleep

from selenium import webdriver


class TestDebug:
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = '127.0.0.1:9432'
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()


    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("我是一名共产党")
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        sleep(3)

    def test_haoso(self):
        self.driver.get("http://www.so.com")
        self.driver.find_element_by_css_selector('#input').send_keys("我打开了好搜")
        sleep(3)

