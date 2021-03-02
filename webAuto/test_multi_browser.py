import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestMultiBrowser:
    def setup(self):
        #运行时：先set browser=chrome，再执行pytest xxxx -vs
        browser = os.getenv('browser')
        if browser == 'chrome':
            option = webdriver.ChromeOptions()
            option.debugger_address = '127.0.0.1:9432'
            self.driver = webdriver.Chrome(options=option)
        else:
            option = webdriver.FirefoxOptions()
            option.debugger_address = '127.0.0.1:9433'
            self.driver = webdriver.Firefox(options=option)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector('#menu_contacts').click()
        # 等待js加载
        sleep(5)
        self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[-1].click()
        self.driver.find_element_by_id('username').send_keys("张三")
        self.driver.find_element_by_css_selector('[name="acctid"]').send_keys('1111')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('12345678924')
        # self.driver.find_element_by_class_name("qui_btn ww_btn js_btn_save").click()
