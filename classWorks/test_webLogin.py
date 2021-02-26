"""
作业：通过浏览器利用cookie实现企业微信登录
解题思路：
步骤一、通过复用浏览器登录企业微信，获取用户cookie，具体实现思路
1）打开复用浏览器的方法：
cmd命令行窗口：chrome -remote-debugging-port=9432
2) 复用浏览器参数：webdriver.ChromeOptions.debugger_address = '127.0.0.1:9432'
3）打开复用浏览器： webdriver.Chrome(options=上面参数)
4）手动登录企业微信并获取用户cookie，并记录到文本中【ps: 如果想cookie能够长期使用，可以修改cookie的有效时间】

步骤二、取消debug模式浏览器【打开新窗口的浏览器】，将cookie添加到请求中，驱动浏览器打开企业微信，刷新页面，实现利用cookie登录企业微信
1）去掉复用浏览器参数，使用webdriver.Chrome()打开浏览器
2）从文件中读取cookie，并添加到请求中
3）去登录企业微信，登录成功，则实现了cookie登录；否则debug排查代码

"""
import json
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    @pytest.mark.skip
    def test_get_cookie(self):
        "复用浏览器"
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9432'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element_by_id("menu_apps").click()
        # sleep(3)
        cookie = self.driver.get_cookies()
        # print(cookie, type(cookie))
        with open("./cookie.txt", 'w', encoding="utf-8") as f:
            json.dump(cookie, f)


    def test_cookie_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        try:
            with open('./cookie.txt', 'r', encoding='utf-8') as f:
                cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.refresh()
            "登录后的操作"
            WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "menu_customer")))
            self.driver.find_element_by_id("menu_customer").click()
        finally:
            sleep(3)
            self.driver.quit()




