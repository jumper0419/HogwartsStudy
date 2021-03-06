# -*- encoding: UTF-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestApp:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'  # 测试版本
        desired_caps['deviceName'] = 'emulator-5554'  # 设备名
        desired_caps['platformVersion'] = '11.0'  # 系统版本
        desired_caps["appPackage"] = "com.tencent.wework"  # app包名
        desired_caps["appActivity"] = ".launch.LaunchSplashActivity"  # 启动launch Activity
        desired_caps["noReset"] = True  # 不清空数据
        desired_caps["unicodeKeyboard"] = True  # 使用Unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = True  # 键盘隐藏起来
        desired_caps["skipDeviceInitialization"] = True  # 跳过设备初始化，例如安装，权限设置等操作
        desired_caps["skipServerInstallation"] = True  # 跳过uiautomator2server的安装
        desired_caps["settings[waitForIdleTimeout]"] = 0  # 德昂带页面空闲的时间
        desired_caps["newCommandTimeout"] = 300
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()


    def test_daka(self):
        sleep(20)
        daka_locat = (MobileBy.XPATH, "//*[@class='android.view.ViewGroup']//*[@text='工作台']")
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(daka_locat))
        self.driver.find_element(*daka_locat).click()
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.view.ViewGroup']//*[@text='工作台']").click()
        # driver.find_element_by_android_uiautomator(‘new
        # UiScrollable(new
        # UiSelector().’
        # ‘scrollable(true).instance(0)).’
        # ‘scrollIntoView(new
        # UiSelector().textContains(“病人”).’
        # ‘instance(0));’).click()
