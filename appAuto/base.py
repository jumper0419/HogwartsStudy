from appium import webdriver


class Base:
    def setup(self):
        desired_caps = {
            'platformName': 'Android',  # 测试版本
            'deviceName': 'emulator-5554',  # 设备名
            'platformVersion': '11.0',  # 系统版本
            "appPackage": "com.android.chrome",  # app包名
            "appActivity": "com.google.android.apps.chrome.Main",  # 启动launch Activity
            "noReset": True,  # 不清空数据
            "unicodeKeyboard": True,  # 使用Unicode编码方式发送字符串
            "resetKeyboard": True,  # 键盘隐藏起来
            "skipDeviceInitialization": True,  # 跳过安装，权限设置等操作
        }

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()