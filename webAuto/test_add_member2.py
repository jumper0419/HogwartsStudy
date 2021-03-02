import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddMember:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = '127.0.0.1:9432'
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_add_member(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_css_selector('#menu_contacts').click()
        sleep(1)
        # 等待js加载
        def wait_add(driver):
            eles = driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')
            eles[-1].click()
            add_eles = driver.find_elements(By.XPATH, "//*[@id='memberAdd_acctid']")
            return len(add_eles) >= 1

        WebDriverWait(self.driver, 30).until(wait_add)
        # self.driver.find_elements(By.XPATH, '//*[@class="qui_btn ww_btn js_add_member"]')[-1].click()
        self.driver.find_element_by_id('username').send_keys("张三")
        self.driver.find_element_by_css_selector('[name="acctid"]').send_keys('1113')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys('12345678926')
        self.driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']")[0].click()
