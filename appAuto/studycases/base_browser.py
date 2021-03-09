from appium import webdriver


class Base:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',  # 测试版本
            'deviceName': 'emulator-5554',  # 设备名
            'platformVersion': '11.0',  # 系统版本
            "noReset": True,  # 不清空数据
            "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
            "resetKeyboard": True,  # 键盘隐藏起来
            "skipDeviceInitialization": True,  # 跳过安装，权限设置等操作
            "browserName": "Chrome",
            "chromedriverExecutable": "",
            "autoGrantPermissions": True,
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()